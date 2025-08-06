#!/usr/bin/env python3
"""Hyperliquid services for CoinGlass API v4"""

from typing import Dict, Any, Optional
from .base import CoinglassAPIBase


class HyperliquidMarketDataService(CoinglassAPIBase):
    """Service for Hyperliquid market data"""
    
    def fetch_data(self, symbol: Optional[str] = None) -> Dict[str, Any]:
        """Get Hyperliquid market data
        
        Args:
            symbol: Cryptocurrency symbol (optional)
        """
        endpoint_suffix = "/hyperliquid/market-data"
        params = {}
        if symbol:
            params["symbol"] = symbol
        return self._make_request_with_prefix(endpoint_suffix, params if params else None)


class HyperliquidOpenInterestService(CoinglassAPIBase):
    """Service for Hyperliquid open interest data"""
    
    def fetch_data(self, symbol: str = "BTC") -> Dict[str, Any]:
        """Get Hyperliquid open interest data
        
        Args:
            symbol: Cryptocurrency symbol (default: BTC)
        """
        endpoint_suffix = "/hyperliquid/open-interest"
        params = {"symbol": symbol}
        return self._make_request_with_prefix(endpoint_suffix, params)


class HyperliquidFundingRatesService(CoinglassAPIBase):
    """Service for Hyperliquid funding rates"""
    
    def fetch_data(self, symbol: Optional[str] = None) -> Dict[str, Any]:
        """Get Hyperliquid funding rates
        
        Args:
            symbol: Cryptocurrency symbol (optional)
        """
        endpoint_suffix = "/hyperliquid/funding-rates"
        params = {}
        if symbol:
            params["symbol"] = symbol
        return self._make_request_with_prefix(endpoint_suffix, params if params else None)


class HyperliquidLiquidationsService(CoinglassAPIBase):
    """Service for Hyperliquid liquidations data"""
    
    def fetch_data(self, symbol: Optional[str] = None, timeframe: str = "24h") -> Dict[str, Any]:
        """Get Hyperliquid liquidations data
        
        Args:
            symbol: Cryptocurrency symbol (optional)
            timeframe: Time frame (default: 24h)
        """
        endpoint_suffix = "/hyperliquid/liquidations"
        params = {"timeframe": timeframe}
        if symbol:
            params["symbol"] = symbol
        return self._make_request_with_prefix(endpoint_suffix, params)


class HyperliquidVolumeService(CoinglassAPIBase):
    """Service for Hyperliquid volume data"""
    
    def fetch_data(self, symbol: Optional[str] = None, timeframe: str = "24h") -> Dict[str, Any]:
        """Get Hyperliquid volume data
        
        Args:
            symbol: Cryptocurrency symbol (optional)
            timeframe: Time frame (default: 24h)
        """
        endpoint_suffix = "/hyperliquid/volume"
        params = {"timeframe": timeframe}
        if symbol:
            params["symbol"] = symbol
        return self._make_request_with_prefix(endpoint_suffix, params)


class HyperliquidOrderbookService(CoinglassAPIBase):
    """Service for Hyperliquid orderbook data"""
    
    def fetch_data(self, symbol: str = "BTC", depth: int = 20) -> Dict[str, Any]:
        """Get Hyperliquid orderbook data
        
        Args:
            symbol: Cryptocurrency symbol (default: BTC)
            depth: Orderbook depth (default: 20)
        """
        endpoint_suffix = "/hyperliquid/orderbook"
        params = {"symbol": symbol, "depth": depth}
        return self._make_request_with_prefix(endpoint_suffix, params)


class HyperliquidTradesService(CoinglassAPIBase):
    """Service for Hyperliquid recent trades"""
    
    def fetch_data(self, symbol: str = "BTC", limit: int = 100) -> Dict[str, Any]:
        """Get Hyperliquid recent trades
        
        Args:
            symbol: Cryptocurrency symbol (default: BTC)
            limit: Number of trades to fetch (default: 100)
        """
        endpoint_suffix = "/hyperliquid/trades"
        params = {"symbol": symbol, "limit": limit}
        return self._make_request_with_prefix(endpoint_suffix, params)