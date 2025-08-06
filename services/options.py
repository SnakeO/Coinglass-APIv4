from typing import Any, Dict, Optional
from services.base import CoinglassAPIBase


class OptionsBaseService(CoinglassAPIBase):
    """Base service for options-related endpoints"""
    _endpoint_prefix = "/option"

    def _make_request_with_prefix(self, endpoint_suffix: str, params: dict | None = None) -> dict:
        endpoint = f"{self._endpoint_prefix}{endpoint_suffix}"
        return self._make_request(endpoint, params)


class MaxPainService(OptionsBaseService):
    """Service for fetching options max pain data"""
    
    def fetch_data(self, symbol: str) -> Dict[str, Any]:
        endpoint_suffix = "/max-pain"
        params = {"symbol": symbol}
        return self._make_request_with_prefix(endpoint_suffix, params)


class OptionsInfoService(OptionsBaseService):
    """Service for fetching comprehensive options data"""
    
    def fetch_data(self, symbol: str) -> Dict[str, Any]:
        endpoint_suffix = "/info"
        params = {"symbol": symbol}
        return self._make_request_with_prefix(endpoint_suffix, params)


class OptionsExchangeOIHistoryService(OptionsBaseService):
    """Service for fetching historical options open interest by exchange"""
    
    def fetch_data(self, symbol: str, unit: Optional[str] = None, range: Optional[str] = None) -> Dict[str, Any]:
        endpoint_suffix = "/exchange-oi-history"
        params = {"symbol": symbol}
        if unit:
            params["unit"] = unit
        if range:
            params["range"] = range
        return self._make_request_with_prefix(endpoint_suffix, params)


class OptionsExchangeVolHistoryService(OptionsBaseService):
    """Service for fetching historical options trading volume by exchange"""
    
    def fetch_data(self, symbol: str, unit: Optional[str] = None, range: Optional[str] = None) -> Dict[str, Any]:
        endpoint_suffix = "/exchange-vol-history"
        params = {"symbol": symbol}
        if unit:
            params["unit"] = unit
        if range:
            params["range"] = range
        return self._make_request_with_prefix(endpoint_suffix, params)


class OptionsFlowService(OptionsBaseService):
    """Service for options flow data"""
    
    def fetch_data(self, symbol: str = "BTC", exchange: Optional[str] = None) -> Dict[str, Any]:
        endpoint_suffix = "/flow"
        params = {"symbol": symbol}
        if exchange:
            params["exchange"] = exchange
        return self._make_request_with_prefix(endpoint_suffix, params)


class OptionsGammaExposureService(OptionsBaseService):
    """Service for options gamma exposure"""
    
    def fetch_data(self, symbol: str = "BTC") -> Dict[str, Any]:
        endpoint_suffix = "/gamma-exposure"
        params = {"symbol": symbol}
        return self._make_request_with_prefix(endpoint_suffix, params)


class OptionsImpliedVolatilityService(OptionsBaseService):
    """Service for options implied volatility"""
    
    def fetch_data(self, symbol: str = "BTC") -> Dict[str, Any]:
        endpoint_suffix = "/implied-volatility"
        params = {"symbol": symbol}
        return self._make_request_with_prefix(endpoint_suffix, params)


class OptionsVolumeByStrikeService(OptionsBaseService):
    """Service for options volume by strike price"""
    
    def fetch_data(self, symbol: str = "BTC", expiry: Optional[str] = None) -> Dict[str, Any]:
        endpoint_suffix = "/volume-by-strike"
        params = {"symbol": symbol}
        if expiry:
            params["expiry"] = expiry
        return self._make_request_with_prefix(endpoint_suffix, params)


class OptionsOpenInterestByStrikeService(OptionsBaseService):
    """Service for options open interest by strike price"""
    
    def fetch_data(self, symbol: str = "BTC", expiry: Optional[str] = None) -> Dict[str, Any]:
        endpoint_suffix = "/oi-by-strike"
        params = {"symbol": symbol}
        if expiry:
            params["expiry"] = expiry
        return self._make_request_with_prefix(endpoint_suffix, params)


class OptionsPutCallRatioService(OptionsBaseService):
    """Service for options put/call ratio"""
    
    def fetch_data(self, symbol: str = "BTC", timeframe: str = "24h") -> Dict[str, Any]:
        endpoint_suffix = "/put-call-ratio"
        params = {"symbol": symbol, "timeframe": timeframe}
        return self._make_request_with_prefix(endpoint_suffix, params)