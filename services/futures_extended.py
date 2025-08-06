#!/usr/bin/env python3
"""Extended futures services for CoinGlass API v4"""

from typing import Dict, Any, Optional
from .base import CoinglassAPIBase


class FuturesVolumeService(CoinglassAPIBase):
    """Service for futures volume data"""
    
    def fetch_data(self, symbol: str = "BTC", exchange: Optional[str] = None) -> Dict[str, Any]:
        """Get futures volume data
        
        Args:
            symbol: Cryptocurrency symbol (default: BTC)
            exchange: Exchange name (optional)
        """
        endpoint_suffix = "/futures/volume"
        params = {"symbol": symbol}
        if exchange:
            params["exchange"] = exchange
        return self._make_request_with_prefix(endpoint_suffix, params)


class FuturesOpenInterestAggregatedService(CoinglassAPIBase):
    """Service for aggregated futures open interest"""
    
    def fetch_data(self, symbol: str = "BTC") -> Dict[str, Any]:
        """Get aggregated futures open interest
        
        Args:
            symbol: Cryptocurrency symbol (default: BTC)
        """
        endpoint_suffix = "/futures/open-interest-aggregated"
        params = {"symbol": symbol}
        return self._make_request_with_prefix(endpoint_suffix, params)


class FuturesBasisService(CoinglassAPIBase):
    """Service for futures basis data"""
    
    def fetch_data(self, symbol: str = "BTC", exchange: Optional[str] = None) -> Dict[str, Any]:
        """Get futures basis data
        
        Args:
            symbol: Cryptocurrency symbol (default: BTC)
            exchange: Exchange name (optional)
        """
        endpoint_suffix = "/futures/basis"
        params = {"symbol": symbol}
        if exchange:
            params["exchange"] = exchange
        return self._make_request_with_prefix(endpoint_suffix, params)


class FuturesGlobalAverageService(CoinglassAPIBase):
    """Service for futures global average price"""
    
    def fetch_data(self, symbol: str = "BTC") -> Dict[str, Any]:
        """Get futures global average price
        
        Args:
            symbol: Cryptocurrency symbol (default: BTC)
        """
        endpoint_suffix = "/futures/global-average-price"
        params = {"symbol": symbol}
        return self._make_request_with_prefix(endpoint_suffix, params)


class FuturesTopAccountRatioService(CoinglassAPIBase):
    """Service for futures top account ratio"""
    
    def fetch_data(self, symbol: str = "BTC", exchange: str = "Binance") -> Dict[str, Any]:
        """Get futures top account ratio
        
        Args:
            symbol: Cryptocurrency symbol (default: BTC)
            exchange: Exchange name (default: Binance)
        """
        endpoint_suffix = "/futures/top-account-ratio"
        params = {"symbol": symbol, "exchange": exchange}
        return self._make_request_with_prefix(endpoint_suffix, params)


class FuturesTopPositionRatioService(CoinglassAPIBase):
    """Service for futures top position ratio"""
    
    def fetch_data(self, symbol: str = "BTC", exchange: str = "Binance") -> Dict[str, Any]:
        """Get futures top position ratio
        
        Args:
            symbol: Cryptocurrency symbol (default: BTC)
            exchange: Exchange name (default: Binance)
        """
        endpoint_suffix = "/futures/top-position-ratio"
        params = {"symbol": symbol, "exchange": exchange}
        return self._make_request_with_prefix(endpoint_suffix, params)


class FuturesActiveBuyingSelling12HService(CoinglassAPIBase):
    """Service for futures active buying/selling 12H data"""
    
    def fetch_data(self, symbol: str = "BTC", exchange: Optional[str] = None) -> Dict[str, Any]:
        """Get futures active buying/selling 12H data
        
        Args:
            symbol: Cryptocurrency symbol (default: BTC)
            exchange: Exchange name (optional)
        """
        endpoint_suffix = "/futures/active-buying-selling-12h"
        params = {"symbol": symbol}
        if exchange:
            params["exchange"] = exchange
        return self._make_request_with_prefix(endpoint_suffix, params)


class FuturesActiveBuyingSelling24HService(CoinglassAPIBase):
    """Service for futures active buying/selling 24H data"""
    
    def fetch_data(self, symbol: str = "BTC", exchange: Optional[str] = None) -> Dict[str, Any]:
        """Get futures active buying/selling 24H data
        
        Args:
            symbol: Cryptocurrency symbol (default: BTC)
            exchange: Exchange name (optional)
        """
        endpoint_suffix = "/futures/active-buying-selling-24h"
        params = {"symbol": symbol}
        if exchange:
            params["exchange"] = exchange
        return self._make_request_with_prefix(endpoint_suffix, params)


class FuturesBubbleColorService(CoinglassAPIBase):
    """Service for futures bubble color data"""
    
    def fetch_data(self, symbol: str = "BTC", exchange: Optional[str] = None) -> Dict[str, Any]:
        """Get futures bubble color data (volatility/volume analysis)
        
        Args:
            symbol: Cryptocurrency symbol (default: BTC)
            exchange: Exchange name (optional)
        """
        endpoint_suffix = "/futures/bubble-color"
        params = {"symbol": symbol}
        if exchange:
            params["exchange"] = exchange
        return self._make_request_with_prefix(endpoint_suffix, params)


class FuturesStablesFundingRatesService(CoinglassAPIBase):
    """Service for stablecoins funding rates in futures"""
    
    def fetch_data(self, stablecoin: str = "USDT") -> Dict[str, Any]:
        """Get stablecoins funding rates
        
        Args:
            stablecoin: Stablecoin symbol (default: USDT)
        """
        endpoint_suffix = "/futures/stables-funding-rates"
        params = {"stablecoin": stablecoin}
        return self._make_request_with_prefix(endpoint_suffix, params)