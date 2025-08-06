from typing import Any, Dict
from services.base import CoinglassAPIBase


class FuturesMarketsBaseService(CoinglassAPIBase):
    """Base service for futures market data endpoints"""
    _endpoint_prefix = "/futures"

    def _make_request_with_prefix(self, endpoint_suffix: str, params: dict | None = None) -> dict:
        endpoint = f"{self._endpoint_prefix}{endpoint_suffix}"
        return self._make_request(endpoint, params)


class CoinsMarketsService(FuturesMarketsBaseService):
    """Service for fetching performance metrics for all futures coins"""
    
    def fetch_data(self) -> Dict[str, Any]:
        endpoint_suffix = "/coins-markets"
        return self._make_request_with_prefix(endpoint_suffix)


class PairsMarketsService(FuturesMarketsBaseService):
    """Service for fetching performance metrics for all futures trading pairs"""
    
    def fetch_data(self) -> Dict[str, Any]:
        endpoint_suffix = "/pairs-markets"
        return self._make_request_with_prefix(endpoint_suffix)


class CoinsPriceChangeService(FuturesMarketsBaseService):
    """Service for fetching price change percentages across multiple timeframes"""
    
    def fetch_data(self) -> Dict[str, Any]:
        endpoint_suffix = "/coins-price-change"
        return self._make_request_with_prefix(endpoint_suffix)


class DelistedPairsService(FuturesMarketsBaseService):
    """Service for fetching list of delisted futures trading pairs"""
    
    def fetch_data(self) -> Dict[str, Any]:
        endpoint_suffix = "/delisted-pairs"
        return self._make_request_with_prefix(endpoint_suffix)


class ExchangeRankService(FuturesMarketsBaseService):
    """Service for fetching futures exchange rankings"""
    
    def fetch_data(self) -> Dict[str, Any]:
        endpoint_suffix = "/exchange-rank"
        return self._make_request_with_prefix(endpoint_suffix)