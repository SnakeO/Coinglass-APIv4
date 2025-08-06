from typing import Any, Dict
from services.base import CoinglassAPIBase


class ETFBaseService(CoinglassAPIBase):
    """Base service for ETF-related endpoints"""
    _endpoint_prefix = "/etf"

    def _make_request_with_prefix(self, endpoint_suffix: str, params: dict | None = None) -> dict:
        endpoint = f"{self._endpoint_prefix}{endpoint_suffix}"
        return self._make_request(endpoint, params)


class BitcoinETFListService(ETFBaseService):
    """Service for fetching list of Bitcoin ETFs"""
    
    def fetch_data(self) -> Dict[str, Any]:
        endpoint_suffix = "/bitcoin/list"
        return self._make_request_with_prefix(endpoint_suffix)


class BitcoinETFNetAssetsHistoryService(ETFBaseService):
    """Service for fetching historical net assets for Bitcoin ETFs"""
    
    def fetch_data(self) -> Dict[str, Any]:
        endpoint_suffix = "/bitcoin/net-assets/history"
        return self._make_request_with_prefix(endpoint_suffix)


class BitcoinETFFlowHistoryService(ETFBaseService):
    """Service for fetching historical flows for Bitcoin ETFs"""
    
    def fetch_data(self) -> Dict[str, Any]:
        endpoint_suffix = "/bitcoin/flow-history"
        return self._make_request_with_prefix(endpoint_suffix)


class BitcoinETFPremiumDiscountHistoryService(ETFBaseService):
    """Service for fetching premium/discount history for Bitcoin ETFs"""
    
    def fetch_data(self) -> Dict[str, Any]:
        endpoint_suffix = "/bitcoin/premium-discount/history"
        return self._make_request_with_prefix(endpoint_suffix)


class BitcoinETFHistoryService(ETFBaseService):
    """Service for fetching aggregate Bitcoin ETF metrics"""
    
    def fetch_data(self) -> Dict[str, Any]:
        endpoint_suffix = "/bitcoin/history"
        return self._make_request_with_prefix(endpoint_suffix)


class BitcoinETFPriceHistoryService(ETFBaseService):
    """Service for fetching Bitcoin ETF price history"""
    
    def fetch_data(self) -> Dict[str, Any]:
        endpoint_suffix = "/bitcoin/price/history"
        return self._make_request_with_prefix(endpoint_suffix)


class BitcoinETFDetailService(ETFBaseService):
    """Service for fetching detailed Bitcoin ETF information"""
    
    def fetch_data(self) -> Dict[str, Any]:
        endpoint_suffix = "/bitcoin/detail"
        return self._make_request_with_prefix(endpoint_suffix)


class BitcoinETFAUMService(ETFBaseService):
    """Service for fetching Bitcoin ETF Assets Under Management"""
    
    def fetch_data(self) -> Dict[str, Any]:
        endpoint_suffix = "/bitcoin/aum"
        return self._make_request_with_prefix(endpoint_suffix)


class EthereumETFListService(ETFBaseService):
    """Service for fetching list of Ethereum ETFs"""
    
    def fetch_data(self) -> Dict[str, Any]:
        endpoint_suffix = "/ethereum/list"
        return self._make_request_with_prefix(endpoint_suffix)


class EthereumETFNetAssetsHistoryService(ETFBaseService):
    """Service for fetching historical net assets for Ethereum ETFs"""
    
    def fetch_data(self) -> Dict[str, Any]:
        endpoint_suffix = "/ethereum/net-assets/history"
        return self._make_request_with_prefix(endpoint_suffix)


class EthereumETFFlowHistoryService(ETFBaseService):
    """Service for fetching historical flows for Ethereum ETFs"""
    
    def fetch_data(self) -> Dict[str, Any]:
        endpoint_suffix = "/ethereum/flow-history"
        return self._make_request_with_prefix(endpoint_suffix)


class HKBitcoinETFFlowHistoryService(CoinglassAPIBase):
    """Service for fetching Hong Kong Bitcoin ETF flow history"""
    
    def fetch_data(self) -> Dict[str, Any]:
        endpoint = "/hk-etf/bitcoin/flow-history"
        return self._make_request(endpoint)


class GrayscaleHoldingsListService(CoinglassAPIBase):
    """Service for fetching Grayscale trust holdings"""
    
    def fetch_data(self) -> Dict[str, Any]:
        endpoint = "/grayscale/holdings/list"
        return self._make_request(endpoint)


class GrayscalePremiumHistoryService(CoinglassAPIBase):
    """Service for fetching Grayscale premium/discount history"""
    
    def fetch_data(self, symbol: str = None) -> Dict[str, Any]:
        endpoint = "/grayscale/premium/history"
        params = {"symbol": symbol} if symbol else None
        return self._make_request(endpoint, params)


class EthereumETFPremiumDiscountHistoryService(ETFBaseService):
    """Service for fetching premium/discount history for Ethereum ETFs"""
    
    def fetch_data(self) -> Dict[str, Any]:
        endpoint_suffix = "/ethereum/premium-discount/history"
        return self._make_request_with_prefix(endpoint_suffix)


class EthereumETFHistoryService(ETFBaseService):
    """Service for fetching aggregate Ethereum ETF metrics"""
    
    def fetch_data(self) -> Dict[str, Any]:
        endpoint_suffix = "/ethereum/history"
        return self._make_request_with_prefix(endpoint_suffix)


class EthereumETFPriceHistoryService(ETFBaseService):
    """Service for fetching Ethereum ETF price history"""
    
    def fetch_data(self) -> Dict[str, Any]:
        endpoint_suffix = "/ethereum/price/history"
        return self._make_request_with_prefix(endpoint_suffix)


class EthereumETFDetailService(ETFBaseService):
    """Service for fetching detailed Ethereum ETF information"""
    
    def fetch_data(self) -> Dict[str, Any]:
        endpoint_suffix = "/ethereum/detail"
        return self._make_request_with_prefix(endpoint_suffix)


class EthereumETFAUMService(ETFBaseService):
    """Service for fetching Ethereum ETF Assets Under Management"""
    
    def fetch_data(self) -> Dict[str, Any]:
        endpoint_suffix = "/ethereum/aum"
        return self._make_request_with_prefix(endpoint_suffix)


class HKEthereumETFFlowHistoryService(CoinglassAPIBase):
    """Service for fetching Hong Kong Ethereum ETF flow history"""
    
    def fetch_data(self) -> Dict[str, Any]:
        endpoint = "/hk-etf/ethereum/flow-history"
        return self._make_request(endpoint)