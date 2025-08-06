#!/usr/bin/env python3
"""On-chain services for CoinGlass API v4"""

from typing import Dict, Any, Optional
from .base import CoinglassAPIBase


class OnchainBaseService(CoinglassAPIBase):
    """Base service for on-chain endpoints"""
    _endpoint_prefix = "/onchain"

    def _make_request_with_prefix(self, endpoint_suffix: str, params: Optional[Dict] = None) -> Dict:
        endpoint = f"{self._endpoint_prefix}{endpoint_suffix}"
        return self._make_request(endpoint, params)


class OnchainAddressBalanceService(OnchainBaseService):
    """Service for on-chain address balance data"""
    
    def fetch_data(self, address: str, chain: str = "BTC") -> Dict[str, Any]:
        """Get on-chain address balance
        
        Args:
            address: Wallet address
            chain: Blockchain (default: BTC)
        """
        endpoint_suffix = "/address-balance"
        params = {"address": address, "chain": chain}
        return self._make_request_with_prefix(endpoint_suffix, params)


class OnchainTransactionVolumeService(OnchainBaseService):
    """Service for on-chain transaction volume"""
    
    def fetch_data(self, chain: str = "BTC", timeframe: str = "24h") -> Dict[str, Any]:
        """Get on-chain transaction volume
        
        Args:
            chain: Blockchain (default: BTC)
            timeframe: Time frame (default: 24h)
        """
        endpoint_suffix = "/transaction-volume"
        params = {"chain": chain, "timeframe": timeframe}
        return self._make_request_with_prefix(endpoint_suffix, params)


class OnchainActiveAddressesService(OnchainBaseService):
    """Service for on-chain active addresses"""
    
    def fetch_data(self, chain: str = "BTC", timeframe: str = "24h") -> Dict[str, Any]:
        """Get on-chain active addresses count
        
        Args:
            chain: Blockchain (default: BTC)
            timeframe: Time frame (default: 24h)
        """
        endpoint_suffix = "/active-addresses"
        params = {"chain": chain, "timeframe": timeframe}
        return self._make_request_with_prefix(endpoint_suffix, params)


class OnchainHashRateService(OnchainBaseService):
    """Service for on-chain hash rate data"""
    
    def fetch_data(self, chain: str = "BTC") -> Dict[str, Any]:
        """Get on-chain hash rate
        
        Args:
            chain: Blockchain (default: BTC)
        """
        endpoint_suffix = "/hash-rate"
        params = {"chain": chain}
        return self._make_request_with_prefix(endpoint_suffix, params)


class OnchainMiningDifficultyService(OnchainBaseService):
    """Service for on-chain mining difficulty"""
    
    def fetch_data(self, chain: str = "BTC") -> Dict[str, Any]:
        """Get on-chain mining difficulty
        
        Args:
            chain: Blockchain (default: BTC)
        """
        endpoint_suffix = "/mining-difficulty"
        params = {"chain": chain}
        return self._make_request_with_prefix(endpoint_suffix, params)


class OnchainMempoolService(OnchainBaseService):
    """Service for on-chain mempool data"""
    
    def fetch_data(self, chain: str = "BTC") -> Dict[str, Any]:
        """Get on-chain mempool statistics
        
        Args:
            chain: Blockchain (default: BTC)
        """
        endpoint_suffix = "/mempool"
        params = {"chain": chain}
        return self._make_request_with_prefix(endpoint_suffix, params)


class OnchainGasFeesService(OnchainBaseService):
    """Service for on-chain gas fees"""
    
    def fetch_data(self, chain: str = "ETH") -> Dict[str, Any]:
        """Get on-chain gas fees
        
        Args:
            chain: Blockchain (default: ETH)
        """
        endpoint_suffix = "/gas-fees"
        params = {"chain": chain}
        return self._make_request_with_prefix(endpoint_suffix, params)


class OnchainTotalSupplyService(OnchainBaseService):
    """Service for on-chain total supply"""
    
    def fetch_data(self, chain: str = "BTC") -> Dict[str, Any]:
        """Get on-chain total supply
        
        Args:
            chain: Blockchain (default: BTC)
        """
        endpoint_suffix = "/total-supply"
        params = {"chain": chain}
        return self._make_request_with_prefix(endpoint_suffix, params)


class OnchainCirculatingSupplyService(OnchainBaseService):
    """Service for on-chain circulating supply"""
    
    def fetch_data(self, chain: str = "BTC") -> Dict[str, Any]:
        """Get on-chain circulating supply
        
        Args:
            chain: Blockchain (default: BTC)
        """
        endpoint_suffix = "/circulating-supply"
        params = {"chain": chain}
        return self._make_request_with_prefix(endpoint_suffix, params)


class OnchainWhaleTransactionsService(OnchainBaseService):
    """Service for on-chain whale transactions"""
    
    def fetch_data(self, chain: str = "BTC", min_value: float = 1000000) -> Dict[str, Any]:
        """Get on-chain whale transactions
        
        Args:
            chain: Blockchain (default: BTC)
            min_value: Minimum transaction value in USD (default: 1000000)
        """
        endpoint_suffix = "/whale-transactions"
        params = {"chain": chain, "min_value": min_value}
        return self._make_request_with_prefix(endpoint_suffix, params)