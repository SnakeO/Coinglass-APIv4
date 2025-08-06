from typing import Any, Dict, Optional
from services.base import CoinglassAPIBase


class SpotMarketBaseService(CoinglassAPIBase):
    """Base service for spot market endpoints"""
    _endpoint_prefix = "/spot"

    def _make_request_with_prefix(self, endpoint_suffix: str, params: dict | None = None) -> dict:
        endpoint = f"{self._endpoint_prefix}{endpoint_suffix}"
        return self._make_request(endpoint, params)


class SpotSupportedCoinsService(SpotMarketBaseService):
    """Service for fetching supported spot market coins"""
    
    def fetch_data(self) -> Dict[str, Any]:
        endpoint_suffix = "/supported-coins"
        return self._make_request_with_prefix(endpoint_suffix)


class SpotSupportedExchangePairsService(SpotMarketBaseService):
    """Service for fetching supported spot exchanges and trading pairs"""
    
    def fetch_data(self) -> Dict[str, Any]:
        endpoint_suffix = "/supported-exchange-pairs"
        return self._make_request_with_prefix(endpoint_suffix)


class SpotCoinsMarketsService(SpotMarketBaseService):
    """Service for fetching performance metrics for spot market coins"""
    
    def fetch_data(self) -> Dict[str, Any]:
        endpoint_suffix = "/coins-markets"
        return self._make_request_with_prefix(endpoint_suffix)


class SpotPairsMarketsService(SpotMarketBaseService):
    """Service for fetching performance metrics for spot trading pairs"""
    
    def fetch_data(self) -> Dict[str, Any]:
        endpoint_suffix = "/pairs-markets"
        return self._make_request_with_prefix(endpoint_suffix)


class SpotPriceHistoryService(SpotMarketBaseService):
    """Service for fetching historical OHLC price data for spot pairs"""
    
    def fetch_data(self, symbol: str, interval: str) -> Dict[str, Any]:
        endpoint_suffix = "/price/history"
        params = {"symbol": symbol, "interval": interval}
        return self._make_request_with_prefix(endpoint_suffix, params)


class SpotOrderBookBaseService(SpotMarketBaseService):
    """Base service for spot order book endpoints"""
    _endpoint_prefix = "/spot/orderbook"


class SpotOrderBookAskBidsHistoryService(SpotOrderBookBaseService):
    """Service for fetching historical order book bid/ask data"""
    
    def fetch_data(self, symbol: str, interval: str, range: Optional[float] = None) -> Dict[str, Any]:
        endpoint_suffix = "/ask-bids-history"
        params = {"symbol": symbol, "interval": interval}
        if range:
            params["range"] = range
        return self._make_request_with_prefix(endpoint_suffix, params)


class SpotAggregatedOrderBookAskBidsHistoryService(SpotOrderBookBaseService):
    """Service for fetching aggregated order book bid/ask data"""
    
    def fetch_data(self, symbol: str, interval: str, range: Optional[float] = None) -> Dict[str, Any]:
        endpoint_suffix = "/aggregated-ask-bids-history"
        params = {"symbol": symbol, "interval": interval}
        if range:
            params["range"] = range
        return self._make_request_with_prefix(endpoint_suffix, params)


class SpotOrderBookHistoryService(SpotOrderBookBaseService):
    """Service for fetching order book heatmap data"""
    
    def fetch_data(self, symbol: str, interval: str) -> Dict[str, Any]:
        endpoint_suffix = "/history"
        params = {"symbol": symbol, "interval": interval}
        return self._make_request_with_prefix(endpoint_suffix, params)


class SpotLargeLimitOrderService(SpotOrderBookBaseService):
    """Service for fetching current large orders"""
    
    def fetch_data(self, symbol: str) -> Dict[str, Any]:
        endpoint_suffix = "/large-limit-order"
        params = {"symbol": symbol}
        return self._make_request_with_prefix(endpoint_suffix, params)


class SpotLargeLimitOrderHistoryService(SpotOrderBookBaseService):
    """Service for fetching historical large order data"""
    
    def fetch_data(self, symbol: str, interval: str) -> Dict[str, Any]:
        endpoint_suffix = "/large-limit-order-history"
        params = {"symbol": symbol, "interval": interval}
        return self._make_request_with_prefix(endpoint_suffix, params)


class SpotTakerBuySellVolumeHistoryService(SpotMarketBaseService):
    """Service for fetching taker buy/sell volume history"""
    
    def fetch_data(self, symbol: str, interval: str) -> Dict[str, Any]:
        endpoint_suffix = "/taker-buy-sell-volume/history"
        params = {"symbol": symbol, "interval": interval}
        return self._make_request_with_prefix(endpoint_suffix, params)


class SpotAggregatedTakerBuySellVolumeHistoryService(SpotMarketBaseService):
    """Service for fetching aggregated taker buy/sell volume history"""
    
    def fetch_data(self, symbol: str, interval: str) -> Dict[str, Any]:
        endpoint_suffix = "/aggregated-taker-buy-sell-volume/history"
        params = {"symbol": symbol, "interval": interval}
        return self._make_request_with_prefix(endpoint_suffix, params)


class SpotExchangeVolumeService(SpotMarketBaseService):
    """Service for spot exchange volume data"""
    
    def fetch_data(self, exchange: Optional[str] = None) -> Dict[str, Any]:
        endpoint_suffix = "/exchange-volume"
        params = {}
        if exchange:
            params["exchange"] = exchange
        return self._make_request_with_prefix(endpoint_suffix, params if params else None)


class SpotSymbolInfoService(SpotMarketBaseService):
    """Service for spot symbol information"""
    
    def fetch_data(self, symbol: str) -> Dict[str, Any]:
        endpoint_suffix = "/symbol-info"
        params = {"symbol": symbol}
        return self._make_request_with_prefix(endpoint_suffix, params)


class SpotExchangeWalletBalanceService(SpotMarketBaseService):
    """Service for spot exchange wallet balance"""
    
    def fetch_data(self, exchange: str) -> Dict[str, Any]:
        endpoint_suffix = "/exchange-wallet-balance"
        params = {"exchange": exchange}
        return self._make_request_with_prefix(endpoint_suffix, params)


class SpotNetflowService(SpotMarketBaseService):
    """Service for spot exchange netflow data"""
    
    def fetch_data(self, symbol: str = "BTC", exchange: Optional[str] = None) -> Dict[str, Any]:
        endpoint_suffix = "/netflow"
        params = {"symbol": symbol}
        if exchange:
            params["exchange"] = exchange
        return self._make_request_with_prefix(endpoint_suffix, params)


class SpotFundFlowService(SpotMarketBaseService):
    """Service for spot fund flow data"""
    
    def fetch_data(self, symbol: str = "BTC") -> Dict[str, Any]:
        endpoint_suffix = "/fund-flow"
        params = {"symbol": symbol}
        return self._make_request_with_prefix(endpoint_suffix, params)