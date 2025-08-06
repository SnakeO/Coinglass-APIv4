from typing import Any, Dict
from services.base import CoinglassAPIBase


class OpenInterestBaseService(CoinglassAPIBase):
    """Base service for open interest-related endpoints"""
    _endpoint_prefix = "/futures/open-interest"

    def _make_request_with_prefix(self, endpoint_suffix: str, params: dict | None = None) -> dict:
        endpoint = f"{self._endpoint_prefix}{endpoint_suffix}"
        return self._make_request(endpoint, params)


class OpenInterestHistoryService(OpenInterestBaseService):
    """Service for fetching open interest history for a specific trading pair"""
    
    def fetch_data(self, symbol: str, interval: str = "4h") -> Dict[str, Any]:
        endpoint_suffix = "/history"
        params = {"symbol": symbol, "interval": interval}
        return self._make_request_with_prefix(endpoint_suffix, params)


class AggregatedOpenInterestHistoryService(OpenInterestBaseService):
    """Service for fetching aggregated open interest history across all exchanges"""
    
    def fetch_data(self, symbol: str, interval: str = "4h") -> Dict[str, Any]:
        endpoint_suffix = "/aggregated-history"
        params = {"symbol": symbol, "interval": interval}
        return self._make_request_with_prefix(endpoint_suffix, params)


class StablecoinMarginOpenInterestHistoryService(OpenInterestBaseService):
    """Service for fetching stablecoin-margined futures open interest history"""
    
    def fetch_data(self, symbol: str, interval: str = "4h") -> Dict[str, Any]:
        endpoint_suffix = "/aggregated-stablecoin-margin-history"
        params = {"symbol": symbol, "interval": interval}
        return self._make_request_with_prefix(endpoint_suffix, params)


class CoinMarginOpenInterestHistoryService(OpenInterestBaseService):
    """Service for fetching coin-margined futures open interest history"""
    
    def fetch_data(self, symbol: str, interval: str = "4h") -> Dict[str, Any]:
        endpoint_suffix = "/aggregated-coin-margin-history"
        params = {"symbol": symbol, "interval": interval}
        return self._make_request_with_prefix(endpoint_suffix, params)


class OpenInterestExchangeListService(OpenInterestBaseService):
    """Service for fetching current open interest by exchange"""
    
    def fetch_data(self, symbol: str) -> Dict[str, Any]:
        endpoint_suffix = "/exchange-list"
        params = {"symbol": symbol}
        return self._make_request_with_prefix(endpoint_suffix, params)


class OpenInterestExchangeHistoryChartService(OpenInterestBaseService):
    """Service for fetching historical open interest distribution across exchanges"""
    
    def fetch_data(self, symbol: str) -> Dict[str, Any]:
        endpoint_suffix = "/exchange-history-chart"
        params = {"symbol": symbol}
        return self._make_request_with_prefix(endpoint_suffix, params)