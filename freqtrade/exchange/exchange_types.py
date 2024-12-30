from typing import Any, Literal, TypedDict

from freqtrade.enums import CandleType


class FtHas(TypedDict, total=False):
    """
    TypedDict for representing various exchange capabilities and configurations.

    Attributes:
        order_time_in_force (list[str]): List of supported order time-in-force policies.
        exchange_has_overrides (dict[str, bool]): Dictionary indicating if the exchange has specific overrides.
        marketOrderRequiresPrice (bool): Indicates if market orders require a price.
        stoploss_on_exchange (bool): Indicates if stoploss orders are supported on the exchange.
        stop_price_param (str): Parameter name for the stop price.
        stop_price_prop (Literal["stopPrice", "stopLossPrice"]): Property name for the stop price.
        stop_price_type_field (str): Field name for the stop price type.
        stop_price_type_value_mapping (dict): Mapping of stop price type values.
        stoploss_order_types (dict[str, str]): Dictionary of supported stoploss order types.
        ohlcv_params (dict): Parameters for OHLCV data.
        ohlcv_candle_limit (int): Maximum number of OHLCV candles.
        ohlcv_has_history (bool): Indicates if OHLCV history is available.
        ohlcv_partial_candle (bool): Indicates if partial OHLCV candles are supported.
        ohlcv_require_since (bool): Indicates if OHLCV data requires a 'since' parameter.
        ohlcv_volume_currency (str): Currency used for OHLCV volume.
        ohlcv_candle_limit_per_timeframe (dict[str, int]): Maximum number of OHLCV candles per timeframe.
        tickers_have_quoteVolume (bool): Indicates if tickers include quote volume.
        tickers_have_percentage (bool): Indicates if tickers include percentage change.
        tickers_have_bid_ask (bool): Indicates if tickers include bid and ask prices.
        tickers_have_price (bool): Indicates if tickers include price information.
        trades_limit (int): Maximum number of trades.
        trades_pagination (str): Pagination method for trades.
        trades_pagination_arg (str): Argument used for trades pagination.
        trades_has_history (bool): Indicates if trade history is available.
        trades_pagination_overlap (bool): Indicates if trades pagination has overlap.
        l2_limit_range (list[int] | None): Range of supported L2 order book limits.
        l2_limit_range_required (bool): Indicates if L2 limit range is required.
        ccxt_futures_name (str): Name used for futures in CCXT (usually 'swap').
        mark_ohlcv_price (str): Price used for mark OHLCV data.
        mark_ohlcv_timeframe (str): Timeframe used for mark OHLCV data.
        funding_fee_timeframe (str): Timeframe for funding fee calculations.
        funding_fee_candle_limit (int): Maximum number of funding fee candles.
        floor_leverage (bool): Indicates if floor leverage is supported.
        needs_trading_fees (bool): Indicates if trading fees are required.
        order_props_in_contracts (list[Literal["amount", "cost", "filled", "remaining"]]): List of order properties in contracts.
        ws_enabled (bool): Indicates if WebSocket is enabled.
    """
    order_time_in_force: list[str]
    exchange_has_overrides: dict[str, bool]
    marketOrderRequiresPrice: bool

    # Stoploss on exchange
    stoploss_on_exchange: bool
    stop_price_param: str
    stop_price_prop: Literal["stopPrice", "stopLossPrice"]
    stop_price_type_field: str
    stop_price_type_value_mapping: dict
    stoploss_order_types: dict[str, str]
    # ohlcv
    ohlcv_params: dict
    ohlcv_candle_limit: int
    ohlcv_has_history: bool
    ohlcv_partial_candle: bool
    ohlcv_require_since: bool
    ohlcv_volume_currency: str
    ohlcv_candle_limit_per_timeframe: dict[str, int]
    # Tickers
    tickers_have_quoteVolume: bool
    tickers_have_percentage: bool
    tickers_have_bid_ask: bool
    tickers_have_price: bool
    # Trades
    trades_limit: int
    trades_pagination: str
    trades_pagination_arg: str
    trades_has_history: bool
    trades_pagination_overlap: bool
    # Orderbook
    l2_limit_range: list[int] | None
    l2_limit_range_required: bool
    # Futures
    ccxt_futures_name: str  # usually swap
    mark_ohlcv_price: str
    mark_ohlcv_timeframe: str
    funding_fee_timeframe: str
    funding_fee_candle_limit: int
    floor_leverage: bool
    needs_trading_fees: bool
    order_props_in_contracts: list[Literal["amount", "cost", "filled", "remaining"]]

    # Websocket control
    ws_enabled: bool


class Ticker(TypedDict):
    symbol: str
    ask: float | None
    askVolume: float | None
    bid: float | None
    bidVolume: float | None
    last: float | None
    quoteVolume: float | None
    baseVolume: float | None
    percentage: float | None
    # Several more - only listing required.


Tickers = dict[str, Ticker]


class OrderBook(TypedDict):
    symbol: str
    bids: list[tuple[float, float]]
    asks: list[tuple[float, float]]
    timestamp: int | None
    datetime: str | None
    nonce: int | None


class CcxtBalance(TypedDict):
    free: float
    used: float
    total: float


CcxtBalances = dict[str, CcxtBalance]


class CcxtPosition(TypedDict):
    symbol: str
    side: str
    contracts: float
    leverage: float
    collateral: float | None
    initialMargin: float | None
    liquidationPrice: float | None


CcxtOrder = dict[str, Any]

# pair, timeframe, candleType, OHLCV, drop last?,
OHLCVResponse = tuple[str, str, CandleType, list, bool]
