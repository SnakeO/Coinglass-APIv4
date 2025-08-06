from typing import Any, Dict
from services.base import CoinglassAPIBase


class FundingRateBaseService(CoinglassAPIBase):
    _endpoint_prefix = "/futures/funding-rate"

    def _make_request_with_prefix(self, endpoint_suffix: str, params: dict | None = None) -> dict:
        endpoint = f"{self._endpoint_prefix}{endpoint_suffix}"
        return self._make_request(endpoint, params)


class OHLCHistoryService(FundingRateBaseService):
    def fetch_data(self, symbol: str, interval: str = "1d", exchange: str = "Binance") -> dict:
        endpoint_suffix = "/history"
        params = {"symbol": symbol, "interval": interval}
        return self._make_request_with_prefix(endpoint_suffix, params)


class OIWeightOHLCHistoryService(FundingRateBaseService):
    def fetch_data(self, symbol: str, interval: str = "1d", exchange: str = "Binance") -> dict:
        endpoint_suffix = "/oi-weight-history"
        params = {"symbol": symbol, "interval": interval}
        return self._make_request_with_prefix(endpoint_suffix, params)


class VolWeightOHLCHistoryService(FundingRateBaseService):
    def fetch_data(self, symbol: str, interval: str = "1d", exchange: str = "Binance") -> dict:
        endpoint_suffix = "/vol-weight-history"
        params = {"symbol": symbol, "interval": interval}
        return self._make_request_with_prefix(endpoint_suffix, params)


class ExchangeListService(FundingRateBaseService):
    def fetch_data(self, symbol: str, interval: str = "1d", exchange: str = "Binance") -> dict:
        endpoint_suffix = "/exchange-list"
        params = {"symbol": symbol}
        return self._make_request_with_prefix(endpoint_suffix, params)


class CumulativeExchangeListService(FundingRateBaseService):
    def fetch_data(self, symbol: str, interval: str = "1d", exchange: str = "Binance") -> dict:
        endpoint_suffix = "/accumulated-exchange-list"
        params = {"symbol": symbol}
        return self._make_request_with_prefix(endpoint_suffix, params)
