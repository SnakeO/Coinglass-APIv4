import re
from typing import Type
from services.funding_rates import FundingRateBaseService
from services.general_information import SupportedPairsService


class TopPairsManager:
    """
    Class for managing trading pairs.
    """

    def __init__(self, service: SupportedPairsService = SupportedPairsService()):
        self.service = service

    def get_top_pairs(self, platform: str = 'Binance', top_n: int = 10, clear: bool = True):
        """
        Returns the top N trading pairs for the specified platform.

        :param platform: Name of the trading platform (e.g., 'Binance').
        :param top_n: Number of top pairs to select.
        :param clean: If you want to get top with the information about contracts then you
        need set clear=False (result example: {'BTCUSD_PERP': {'instrumentId': 'BTCUSD_PERP', 'baseAsset': 'BTC', 'quoteAsset': 'USD'}, 'BTCUSD_250328': ...})
        with clear=True you will get ordinary list of pairs.
        :return: List of top N trading pairs (dictionaries).
        """

        data = self.service.fetch_data()

        if data.get("code") != "0":
            raise ValueError(f"Error fetching data: {data.get('msg')}")

        pairs = data.get("data", {}).get(platform, [])

        if not pairs:
            raise ValueError(f"Trading platform '{platform}' not found or contains no data.")

        grouped_pairs = {}
        for pair in pairs:
            key = (pair["baseAsset"], pair["quoteAsset"])
            instrumentId = pair["instrumentId"]
            if key not in grouped_pairs:
                grouped_pairs[key] = {}
            grouped_pairs[key][instrumentId] = pair

        top_pairs = []
        if clear:
            for pair, _ in grouped_pairs.items():
                top_pairs.append(''.join(pair))
        else:
            for _, contracts in grouped_pairs.items():
                top_pairs.append({**contracts})

        return top_pairs[:top_n]


class FundingRateManager:
    def __init__(self, Service: Type[FundingRateBaseService], platform: str = 'Binance', interval: str = '1h'):
        self.service = Service()
        self.platform = platform
        self.interval = interval

    def get_pair_funding_rate_history(self, pair: str, platform: str = 'Binance', interval: str = '1h'):
        """
        Fetches the FundingRate Info for the given trading pair.

        :param pair: The trading pair name.
        :param platform: The platform for data fetching.
        :param interval: The interval for the data.
        :return: The FundingRate data.
        """
        funding_rate_data = self.service.fetch_data(symbol=pair, interval=interval, exchange=platform)

        if funding_rate_data.get("code") != "0":
            raise ValueError(f"Error fetching funding rate data: {funding_rate_data.get('msg')}")

        return funding_rate_data.get("data", [])

    def get_funding_rate(self, top_pairs):
        pairs_funding_rate = []
        for pair_name in top_pairs:
            funding_rate_history = self.get_pair_funding_rate_history(pair_name, self.platform, self.interval)
            pairs_funding_rate.append({'pair': pair_name, 'funding_rate_history': funding_rate_history})

        return pairs_funding_rate
