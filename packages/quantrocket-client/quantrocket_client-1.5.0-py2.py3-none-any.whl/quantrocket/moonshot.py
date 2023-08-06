# Copyright 2017 QuantRocket - All Rights Reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys
from quantrocket.houston import houston
from quantrocket.cli.utils.output import json_to_cli
from quantrocket.cli.utils.files import write_response_to_filepath_or_buffer
from quantrocket.cli.utils.parse import dict_strs_to_dict, dict_to_dict_strs
from quantrocket.exceptions import ParameterError

def backtest(strategies, start_date=None, end_date=None, segment=None, allocations=None,
             nlv=None, params=None, details=None, output="csv", csv=None, filepath_or_buffer=None):
    """
    Backtest one or more strategies.

    By default returns a CSV of backtest results but can also return a PDF tear sheet
    of performance charts.

    If testing multiple strategies, each column in the CSV represents a strategy.
    If testing a single strategy and `details=True`, each column in the CSV
    represents a security in the strategy universe.

    Parameters
    ----------
    strategies : list of str, required
        one or more strategy codes

    start_date : str (YYYY-MM-DD), optional
        the backtest start date (default is to use all available history)

    end_date : str (YYYY-MM-DD), optional
        the backtest end date (default is to use all available history)

    segment : str, optional
        backtest in date segments of this size, to reduce memory usage
        (use Pandas frequency string, e.g. 'A' for annual segments or 'Q'
        for quarterly segments)

    allocations : dict of CODE:FLOAT, optional
        the allocation for each strategy, passed as {code:allocation} (default
        allocation is 1.0 / number of strategies)

    nlv : dict of CURRENCY:NLV, optional
        the NLV (net liquidation value, i.e. account balance) to assume for
        the backtest, expressed in each currency represented in the backtest (pass
        as {currency:nlv})

    params : dict of PARAM:VALUE, optional
        one or more strategy params to set on the fly before backtesting
        (pass as {param:value})

    details : bool
        return detailed results for all securities instead of aggregating to
        strategy level (only supported for single-strategy backtests)

    output : str, required
        the output format (choices are csv or pdf)

    csv : bool
       DEPRECATED: this argument will be removed in a future version. This argument
       may be omitted as CSV is the default.

    filepath_or_buffer : str, optional
        the location to write the results file (omit to write to stdout)

    Returns
    -------
    None
    """
    output = output or "csv"

    if output not in ("csv", "pdf"):
        raise ValueError("invalid output: {0} (choices are csv or pdf".format(output))

    if csv is not None:
        import warnings
        warnings.warn(
            "the `csv` argument is deprecated and will removed in a future version; "
            "this argument may be omitted as csv is the default", DeprecationWarning)

    _params = {}

    if strategies:
        _params["strategies"] = strategies
    if start_date:
        _params["start_date"] = start_date
    if end_date:
        _params["end_date"] = end_date
    if segment:
        _params["segment"] = segment
    if allocations:
        _params["allocations"] = dict_to_dict_strs(allocations)
    if nlv:
        _params["nlv"] = dict_to_dict_strs(nlv)
    if details:
        _params["details"] = details
    if params:
        _params["params"] = dict_to_dict_strs(params)

    response = houston.post("/moonshot/backtests.{0}".format(output),
                            params=_params, timeout=60*60*24)

    houston.raise_for_status_with_json(response)

    filepath_or_buffer = filepath_or_buffer or sys.stdout
    write_response_to_filepath_or_buffer(filepath_or_buffer, response)

def _cli_backtest(*args, **kwargs):
    allocations = kwargs.get("allocations", None)
    if allocations:
        kwargs["allocations"] = dict_strs_to_dict(*allocations)
    nlv = kwargs.get("nlv", None)
    if nlv:
        kwargs["nlv"] = dict_strs_to_dict(*nlv)
    params = kwargs.get("params", None)
    if params:
        kwargs["params"] = dict_strs_to_dict(*params)
    return json_to_cli(backtest, *args, **kwargs)

def read_moonshot_csv(filepath_or_buffer):
    """
    Load a Moonshot backtest CSV into a DataFrame.

    Parameters
    ----------
    filepath_or_buffer : string or file-like, required
        path to CSV

    Returns
    -------
    DataFrame
        a multi-index (Field, Date[, Time]) DataFrame of backtest
        results, with conids or strategy codes as columns

    Examples
    --------
    >>> results = read_moonshot_csv("moonshot_backtest.csv")
    >>> returns = results.loc["Return"]
    """
    try:
        import pandas as pd
    except ImportError:
        raise ImportError("pandas must be installed to use this function")

    results = pd.read_csv(filepath_or_buffer, parse_dates=["Date"])
    index_cols = ["Field", "Date"]
    if "Time" in results.columns:
        index_cols.append("Time")
    results = results.set_index(index_cols)

    fields_in_results = results.index.get_level_values("Field").unique()

    # Cast to float
    float_fields = [
        "Return",
        "Signal",
        "Weight",
        "NetExposure",
        "Trade",
        "Commission",
        "Slippage",
        "Benchmark",
        "AbsWeight",
        "AbsExposure",
        "TotalHoldings",

    ]
    for field in float_fields:
        if field in fields_in_results:
            results.loc[[field]] = results.loc[[field]].astype(pd.np.float64)

    return results

def intraday_to_daily(results):
    """
    Roll up a DataFrame of intraday performance results to daily, dropping
    the "Time" level from the multi-index.

    Parameters
    ----------
    results : DataFrame, required
         a DataFrame of intraday Moonshot backtest results, with a "Time" level
         in the index

    Returns
    -------
    DataFrame
        a DataFrame of daily Moonshot backtest results, without a "Time" level in
        the index

    Examples
    --------
    >>> intraday_results = read_moonshot_csv("moonshot_intraday_backtest.csv")
    >>> daily_results = intraday_to_daily(intraday_results)
    """
    try:
        import pandas as pd
    except ImportError:
        raise ImportError("pandas must be installed to use this function")

    if "Time" not in results.index.names:
        raise ParameterError("results DataFrame must have 'Time' level in index")

    fields_in_results = results.index.get_level_values("Field").unique()

    daily_results = {}

    # how to aggregate by field
    aggregation_methods = {
        "sum": ["Return", "Trade", "Commission", "Slippage"],
        "max": ["AbsExposure", "TotalHoldings", "AbsWeight"],
        "mean": ["NetExposure", "Weight"],
        "last": ["Benchmark"],
    }

    for aggregation_method, fields_to_aggregate in aggregation_methods.items():
        for field in fields_to_aggregate:
            if field not in fields_in_results:
                continue

            field_results = results.loc[field]
            grouped = field_results.groupby(field_results.index.get_level_values("Date"))
            daily_results[field] = getattr(grouped, aggregation_method)()

    daily_results = pd.concat(daily_results, names=["Field","Date"])
    return daily_results

def scan_parameters(strategies, start_date=None, end_date=None, segment=None,
                    param1=None, vals1=None, param2=None, vals2=None,
                    allocations=None, nlv=None, params=None, output="csv",
                    csv=None, filepath_or_buffer=None):
    """
    Run a parameter scan for one or more strategies.

    By default returns a CSV of scan results but can also return a PDF tear sheet.

    Parameters
    ----------
    strategies : list of str, required
        one or more strategy codes

    start_date : str (YYYY-MM-DD), optional
        the backtest start date (default is to use all available history)

    end_date : str (YYYY-MM-DD), optional
        the backtest end date (default is to use all available history)

    segment : str, optional
        backtest in date segments of this size, to reduce memory usage
        (use Pandas frequency string, e.g. 'A' for annual segments or 'Q'
        for quarterly segments)

    param1 : str, required
        the name of the parameter to test (a class attribute on the strategy)

    vals1 : list of int/float/str/tuple, required
        parameter values to test (values can be ints, floats, strings, False,
        True, None, 'default' (to test current param value), or lists of
        ints/floats/strings)

    param2 : str, optional
        name of a second parameter to test (for 2-D parameter scans)

    vals2 : list of int/float/str/tuple, optional
        values to test for parameter 2 (values can be ints, floats, strings,
        False, True, None, 'default' (to test current param value), or lists
        of ints/floats/strings)

    allocations : dict of CODE:FLOAT, optional
        the allocation for each strategy, passed as {code:allocation} (default
        allocation is 1.0 / number of strategies)

    nlv : dict of CURRENCY:NLV, optional
        the NLV (net liquidation value, i.e. account balance) to assume for
        the backtest, expressed in each currency represented in the backtest (pass
        as {currency:nlv})

    params : dict of PARAM:VALUE, optional
        one or more strategy params to set on the fly before backtesting
        (pass as {param:value})

    output : str, required
        the output format (choices are csv or pdf)

    csv : bool
        DEPRECATED: this argument will be removed in a future version. This argument
        may be omitted as CSV is the default.

    filepath_or_buffer : str, optional
        the location to write the results file (omit to write to stdout)

    Returns
    -------
    None
    """
    output = output or "csv"

    if output not in ("csv", "pdf"):
        raise ValueError("invalid output: {0} (choices are csv or pdf".format(output))

    if csv is not None:
        import warnings
        warnings.warn(
            "the `csv` argument is deprecated and will removed in a future version; "
            "this argument may be omitted as csv is the default", DeprecationWarning)

    _params = {}
    if strategies:
        _params["strategies"] = strategies
    if start_date:
        _params["start_date"] = start_date
    if end_date:
        _params["end_date"] = end_date
    if segment:
        _params["segment"] = segment
    if param1:
        _params["param1"] = param1
    if vals1:
        _params["vals1"] = [str(v) for v in vals1]
    if param2:
        _params["param2"] = param2
    if vals2:
        _params["vals2"] = [str(v) for v in vals2]
    if allocations:
        _params["allocations"] = dict_to_dict_strs(allocations)
    if nlv:
        _params["nlv"] = dict_to_dict_strs(nlv)
    if params:
        _params["params"] = dict_to_dict_strs(params)

    response = houston.post("/moonshot/paramscans.{0}".format(output), params=_params, timeout=60*60*24)

    houston.raise_for_status_with_json(response)

    filepath_or_buffer = filepath_or_buffer or sys.stdout
    write_response_to_filepath_or_buffer(filepath_or_buffer, response)

def _cli_scan_parameters(*args, **kwargs):
    allocations = kwargs.get("allocations", None)
    if allocations:
        kwargs["allocations"] = dict_strs_to_dict(*allocations)
    nlv = kwargs.get("nlv", None)
    if nlv:
        kwargs["nlv"] = dict_strs_to_dict(*nlv)
    params = kwargs.get("params", None)
    if params:
        kwargs["params"] = dict_strs_to_dict(*params)
    return json_to_cli(scan_parameters, *args, **kwargs)

def trade(strategies, accounts=None, review_date=None, output="csv", filepath_or_buffer=None):
    """
    Run one or more strategies and generate orders.

    Allocations are read from configuration (quantrocket.moonshot.allocations.yml).

    Parameters
    ----------
    strategies : list of str, required
        one or more strategy codes

    accounts : list of str, optional
        limit to these accounts

    review_date : str (YYYY-MM-DD), optional
        generate orders as if it were this date, rather than using today's date

    output : str, required
        the output format (choices are csv or json)

    filepath_or_buffer : str, optional
        the location to write the orders file (omit to write to stdout)

    Returns
    -------
    None
    """
    params = {}
    if strategies:
        params["strategies"] = strategies
    if accounts:
        params["accounts"] = accounts
    if review_date:
        params["review_date"] = review_date

    output = output or "csv"

    if output not in ("csv", "json"):
        raise ValueError("invalid output: {0} (choices are csv or json".format(output))

    response = houston.get("/moonshot/orders.{0}".format(output), params=params, timeout=60*5)

    houston.raise_for_status_with_json(response)

    # Don't write a null response to file
    if response.content[:4] == b"null":
        return

    filepath_or_buffer = filepath_or_buffer or sys.stdout
    write_response_to_filepath_or_buffer(filepath_or_buffer, response)

def _cli_trade(*args, **kwargs):
    return json_to_cli(trade, *args, **kwargs)
