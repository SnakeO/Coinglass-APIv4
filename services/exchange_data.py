from typing import Any, Dict, Optional
from services.base import CoinglassAPIBase


class ExchangeDataBaseService(CoinglassAPIBase):
    """Base service for exchange-related endpoints"""
    _endpoint_prefix = "/exchange"

    def _make_request_with_prefix(self, endpoint_suffix: str, params: dict | None = None) -> dict:
        endpoint = f"{self._endpoint_prefix}{endpoint_suffix}"
        return self._make_request(endpoint, params)


class ExchangeAssetsService(ExchangeDataBaseService):
    """Service for fetching on-chain asset reserves held on an exchange"""
    
    def fetch_data(self, exchange: str) -> Dict[str, Any]:
        endpoint_suffix = "/assets"
        params = {"exchange": exchange}
        return self._make_request_with_prefix(endpoint_suffix, params)


class ExchangeBalanceListService(ExchangeDataBaseService):
    """Service for fetching current on-chain balance of an asset across exchanges"""
    
    def fetch_data(self, symbol: str) -> Dict[str, Any]:
        endpoint_suffix = "/balance/list"
        params = {"symbol": symbol}
        return self._make_request_with_prefix(endpoint_suffix, params)


class ExchangeBalanceChartService(ExchangeDataBaseService):
    """Service for fetching historical on-chain balance data for charting"""
    
    def fetch_data(self, symbol: str) -> Dict[str, Any]:
        endpoint_suffix = "/balance/chart"
        params = {"symbol": symbol}
        return self._make_request_with_prefix(endpoint_suffix, params)


class ExchangeChainTxListService(ExchangeDataBaseService):
    """Service for fetching on-chain transfer records for an exchange"""
    
    def fetch_data(self, exchange: str, symbol: Optional[str] = None) -> Dict[str, Any]:
        endpoint_suffix = "/chain/tx/list"
        params = {"exchange": exchange}
        if symbol:
            params["symbol"] = symbol
        return self._make_request_with_prefix(endpoint_suffix, params)


class FuturesIndexBaseService(CoinglassAPIBase):
    """Base service for futures index endpoints"""
    _endpoint_prefix = "/futures"

    def _make_request_with_prefix(self, endpoint_suffix: str, params: dict | None = None) -> dict:
        endpoint = f"{self._endpoint_prefix}{endpoint_suffix}"
        return self._make_request(endpoint, params)


class FuturesRSIListService(FuturesIndexBaseService):
    """Service for fetching RSI values for futures contracts"""
    
    def fetch_data(self) -> Dict[str, Any]:
        endpoint_suffix = "/rsi/list"
        return self._make_request_with_prefix(endpoint_suffix)


class FuturesBasisService(FuturesIndexBaseService):
    """Service for fetching futures basis data"""
    
    def fetch_data(self, symbol: Optional[str] = None) -> Dict[str, Any]:
        endpoint_suffix = "/basis"
        params = {"symbol": symbol} if symbol else None
        return self._make_request_with_prefix(endpoint_suffix, params)


class FuturesWhaleIndexService(FuturesIndexBaseService):
    """Service for fetching Whale Index data"""
    
    def fetch_data(self) -> Dict[str, Any]:
        endpoint_suffix = "/whale-index"
        return self._make_request_with_prefix(endpoint_suffix)


class FuturesCGDIIndexService(FuturesIndexBaseService):
    """Service for fetching CoinGlass Derivatives Index"""
    
    def fetch_data(self) -> Dict[str, Any]:
        endpoint_suffix = "/cgdi-index"
        return self._make_request_with_prefix(endpoint_suffix)


class FuturesCDRIIndexService(FuturesIndexBaseService):
    """Service for fetching CoinGlass Derivatives Risk Index"""
    
    def fetch_data(self) -> Dict[str, Any]:
        endpoint_suffix = "/cdri-index"
        return self._make_request_with_prefix(endpoint_suffix)


class CalendarEconomicDataService(CoinglassAPIBase):
    """Service for fetching economic calendar data"""
    
    def fetch_data(self) -> Dict[str, Any]:
        endpoint = "/calendar/economic_data"
        return self._make_request(endpoint)


class HyperliquidWhaleAlertService(CoinglassAPIBase):
    """Service for fetching Hyperliquid whale alerts"""
    
    def fetch_data(self) -> Dict[str, Any]:
        endpoint = "/hyperliquid/whale-alert"
        return self._make_request(endpoint)


class HyperliquidWhalePositionService(CoinglassAPIBase):
    """Service for fetching Hyperliquid whale positions"""
    
    def fetch_data(self) -> Dict[str, Any]:
        endpoint = "/hyperliquid/whale-position"
        return self._make_request(endpoint)