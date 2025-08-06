
from typing import Any, Dict
from services.base import CoinglassAPIBase

class SupportedCoinsService(CoinglassAPIBase):
    def fetch_data(self) -> Dict[str, Any]:
        endpoint = "/futures/supported-coins"
        return self._make_request(endpoint)


class SupportedPairsService(CoinglassAPIBase):
    def fetch_data(self) -> Dict[str, Any]:
        endpoint = "/futures/supported-exchange-pairs"
        return self._make_request(endpoint)
