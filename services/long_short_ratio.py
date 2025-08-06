from typing import Any, Dict
from services.base import CoinglassAPIBase


class GlobalAccountRatioService(CoinglassAPIBase):
    def fetch_data(self, symbol: str, exchange: str = "Binance", interval: str = "1d") -> Dict[str, Any]:
        endpoint = "/futures/global-long-short-account-ratio/history"
        params = {"symbol": symbol, "interval": interval}
        return self._make_request(endpoint, params)

class TopAccountRatioHistoryService(CoinglassAPIBase):
    def fetch_data(self, symbol: str, exchange: str = "Binance", interval: str = "1d") -> Dict[str, Any]:
        endpoint = "/futures/top-long-short-account-ratio/history"
        params = {"symbol": symbol, "interval": interval}
        return self._make_request(endpoint, params)

class TopPositionRatioHistoryService(CoinglassAPIBase):
    def fetch_data(self, symbol: str, exchange: str = "Binance", interval: str = "1d") -> Dict[str, Any]:
        endpoint = "/futures/top-long-short-position-ratio/history"
        params = {"symbol": symbol, "interval": interval}
        return self._make_request(endpoint, params)

class AggregatedTakerBuySellHistoryService(CoinglassAPIBase):
    def fetch_data(self, symbol: str, exchange: str = "Binance", interval: str = "1d") -> Dict[str, Any]:
        endpoint = "/futures/aggregated-taker-buy-sell-volume/history"
        params = {"symbol": symbol, "interval": interval}
        return self._make_request(endpoint, params)
    
class AggregatedTakerBuySellVolumeHistoryService(CoinglassAPIBase):
    def fetch_data(self, symbol: str, exchange: str = "Binance", interval: str = "1d") -> Dict[str, Any]:
        endpoint = "/futures/aggregated-taker-buy-sell-volume/history"
        params = {"symbol": symbol, "interval": interval}
        return self._make_request(endpoint, params)

class TakerBuySellRatioHistoryService(CoinglassAPIBase):
    def fetch_data(self, symbol: str, exchange: str = "Binance", interval: str = "1d") -> Dict[str, Any]:
        endpoint = "/futures/taker-buy-sell-volume/history"
        params = {"symbol": symbol, "interval": interval}
        return self._make_request(endpoint, params)

class ExchangeTakerBuySellRatioHistoryService(CoinglassAPIBase):
    def fetch_data(self, symbol: str, interval: str = "1d") -> Dict[str, Any]:
        endpoint = "/futures/taker-buy-sell-volume/exchange-list"
        params = {"symbol": symbol}
        return self._make_request(endpoint, params)
