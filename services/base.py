import os
import requests

from abc import ABC, abstractmethod
from typing import Any, Dict, Optional
from dotenv import load_dotenv

load_dotenv()
BASE_API_KEY = os.getenv('BASE_API_KEY', '')


class CoinglassAPIBase(ABC):
    """
    Abstract base class for interacting with the Coinglass API.
    """

    BASE_URL = "https://open-api-v4.coinglass.com/api"

    def __init__(self, api_key: str = BASE_API_KEY):
        self.api_key = api_key

    def _get_headers(self) -> Dict[str, str]:
        return {
            "accept": "application/json",
            "CG-API-KEY": self.api_key,
        }

    def _make_request(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Any:
        url = f"{self.BASE_URL}{endpoint}"
        response = requests.get(url, headers=self._get_headers(), params=params)

        if response.status_code != 200:
            response.raise_for_status()
        return response.json()

    @abstractmethod
    def fetch_data(self, **kwargs) -> Any:
        """
        Abstract method to fetch data from a specific API endpoint.
        """
        pass
