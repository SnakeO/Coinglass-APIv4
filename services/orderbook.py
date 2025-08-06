from typing import Any, Dict, Optional
from services.base import CoinglassAPIBase


class OrderBookBaseService(CoinglassAPIBase):
    """Base service for order book-related endpoints"""
    _endpoint_prefix = "/futures/orderbook"

    def _make_request_with_prefix(self, endpoint_suffix: str, params: dict | None = None) -> dict:
        endpoint = f"{self._endpoint_prefix}{endpoint_suffix}"
        return self._make_request(endpoint, params)


class OrderBookAskBidsHistoryService(OrderBookBaseService):
    """Service for fetching historical order book bid & ask volume"""
    
    def fetch_data(self, symbol: str, interval: str, range: Optional[float] = None) -> Dict[str, Any]:
        endpoint_suffix = "/ask-bids-history"
        params = {"symbol": symbol, "interval": interval}
        if range:
            params["range"] = range
        return self._make_request_with_prefix(endpoint_suffix, params)


class AggregatedOrderBookAskBidsHistoryService(OrderBookBaseService):
    """Service for fetching aggregated order book bid & ask volume"""
    
    def fetch_data(self, symbol: str, interval: str, range: Optional[float] = None) -> Dict[str, Any]:
        endpoint_suffix = "/aggregated-ask-bids-history"
        params = {"symbol": symbol, "interval": interval}
        if range:
            params["range"] = range
        return self._make_request_with_prefix(endpoint_suffix, params)


class OrderBookHistoryService(OrderBookBaseService):
    """Service for fetching order book heatmap (historical depth distribution)"""
    
    def fetch_data(self, symbol: str, interval: str) -> Dict[str, Any]:
        endpoint_suffix = "/history"
        params = {"symbol": symbol, "interval": interval}
        return self._make_request_with_prefix(endpoint_suffix, params)


class LargeLimitOrderService(OrderBookBaseService):
    """Service for fetching current large order book entries"""
    
    def fetch_data(self, symbol: str) -> Dict[str, Any]:
        endpoint_suffix = "/large-limit-order"
        params = {"symbol": symbol}
        return self._make_request_with_prefix(endpoint_suffix, params)


class LargeLimitOrderHistoryService(OrderBookBaseService):
    """Service for fetching historical data of large orders"""
    
    def fetch_data(self, symbol: str, interval: str) -> Dict[str, Any]:
        endpoint_suffix = "/large-limit-order-history"
        params = {"symbol": symbol, "interval": interval}
        return self._make_request_with_prefix(endpoint_suffix, params)