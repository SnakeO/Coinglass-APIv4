from typing import Any, Dict
from services.base import CoinglassAPIBase


class PriceHistoryService(CoinglassAPIBase):
    """Service for fetching historical OHLC price data"""
    
    def fetch_data(self, symbol: str, interval: str = "1h") -> Dict[str, Any]:
        endpoint = "/futures/price/history"
        params = {"symbol": symbol, "interval": interval}
        return self._make_request(endpoint, params)