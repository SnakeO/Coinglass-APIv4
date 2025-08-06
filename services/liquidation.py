from typing import Any, Dict, Optional
from services.base import CoinglassAPIBase


class LiquidationBaseService(CoinglassAPIBase):
    """Base service for liquidation-related endpoints"""
    _endpoint_prefix = "/futures/liquidation"

    def _make_request_with_prefix(self, endpoint_suffix: str, params: dict | None = None) -> dict:
        endpoint = f"{self._endpoint_prefix}{endpoint_suffix}"
        return self._make_request(endpoint, params)


class LiquidationHistoryService(LiquidationBaseService):
    """Service for fetching liquidation history for a specific trading pair"""
    
    def fetch_data(self, symbol: str, interval: str = "1h") -> Dict[str, Any]:
        endpoint_suffix = "/history"
        params = {"symbol": symbol, "interval": interval}
        return self._make_request_with_prefix(endpoint_suffix, params)


class AggregatedLiquidationHistoryService(LiquidationBaseService):
    """Service for fetching aggregated liquidation history across all exchanges"""
    
    def fetch_data(self, symbol: str, interval: str = "1h") -> Dict[str, Any]:
        endpoint_suffix = "/aggregated-history"
        params = {"symbol": symbol, "interval": interval}
        return self._make_request_with_prefix(endpoint_suffix, params)


class LiquidationCoinListService(LiquidationBaseService):
    """Service for fetching list of coins with liquidation data"""
    
    def fetch_data(self) -> Dict[str, Any]:
        endpoint_suffix = "/coin-list"
        return self._make_request_with_prefix(endpoint_suffix)


class LiquidationExchangeListService(LiquidationBaseService):
    """Service for fetching list of exchanges with liquidation data"""
    
    def fetch_data(self) -> Dict[str, Any]:
        endpoint_suffix = "/exchange-list"
        return self._make_request_with_prefix(endpoint_suffix)


class LiquidationOrderService(LiquidationBaseService):
    """Service for fetching recent large liquidation orders"""
    
    def fetch_data(self) -> Dict[str, Any]:
        endpoint_suffix = "/order"
        return self._make_request_with_prefix(endpoint_suffix)


class LiquidationHeatmapModel1Service(LiquidationBaseService):
    """Service for fetching liquidation heatmap data (Model 1)"""
    
    def fetch_data(self, symbol: str) -> Dict[str, Any]:
        endpoint_suffix = "/heatmap/model1"
        params = {"symbol": symbol}
        return self._make_request_with_prefix(endpoint_suffix, params)


class LiquidationHeatmapModel2Service(LiquidationBaseService):
    """Service for fetching liquidation heatmap data (Model 2)"""
    
    def fetch_data(self, symbol: str) -> Dict[str, Any]:
        endpoint_suffix = "/heatmap/model2"
        params = {"symbol": symbol}
        return self._make_request_with_prefix(endpoint_suffix, params)


class LiquidationHeatmapModel3Service(LiquidationBaseService):
    """Service for fetching liquidation heatmap data (Model 3)"""
    
    def fetch_data(self, symbol: str) -> Dict[str, Any]:
        endpoint_suffix = "/heatmap/model3"
        params = {"symbol": symbol}
        return self._make_request_with_prefix(endpoint_suffix, params)


class AggregatedLiquidationHeatmapModel1Service(LiquidationBaseService):
    """Service for fetching aggregated liquidation heatmap data (Model 1)"""
    
    def fetch_data(self, symbol: str) -> Dict[str, Any]:
        endpoint_suffix = "/aggregated-heatmap/model1"
        params = {"symbol": symbol}
        return self._make_request_with_prefix(endpoint_suffix, params)


class AggregatedLiquidationHeatmapModel2Service(LiquidationBaseService):
    """Service for fetching aggregated liquidation heatmap data (Model 2)"""
    
    def fetch_data(self, symbol: str) -> Dict[str, Any]:
        endpoint_suffix = "/aggregated-heatmap/model2"
        params = {"symbol": symbol}
        return self._make_request_with_prefix(endpoint_suffix, params)


class AggregatedLiquidationHeatmapModel3Service(LiquidationBaseService):
    """Service for fetching aggregated liquidation heatmap data (Model 3)"""
    
    def fetch_data(self, symbol: str) -> Dict[str, Any]:
        endpoint_suffix = "/aggregated-heatmap/model3"
        params = {"symbol": symbol}
        return self._make_request_with_prefix(endpoint_suffix, params)


class LiquidationMapService(LiquidationBaseService):
    """Service for fetching liquidation map data"""
    
    def fetch_data(self, symbol: str) -> Dict[str, Any]:
        endpoint_suffix = "/map"
        params = {"symbol": symbol}
        return self._make_request_with_prefix(endpoint_suffix, params)


class AggregatedLiquidationMapService(LiquidationBaseService):
    """Service for fetching aggregated liquidation map data"""
    
    def fetch_data(self, symbol: str) -> Dict[str, Any]:
        endpoint_suffix = "/aggregated-map"
        params = {"symbol": symbol}
        return self._make_request_with_prefix(endpoint_suffix, params)