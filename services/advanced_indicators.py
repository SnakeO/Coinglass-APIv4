#!/usr/bin/env python3
"""Advanced indicators services for CoinGlass API v4"""

from typing import Dict, Any, Optional
from .base import CoinglassAPIBase


class AhrService(CoinglassAPIBase):
    """Service for AHR (Ahr999) indicator"""
    
    def fetch_data(self) -> Dict[str, Any]:
        """Get AHR999 indicator data (Bitcoin valuation metric)"""
        endpoint_suffix = "/indicators/ahr"
        return self._make_request_with_prefix(endpoint_suffix)


class TwoYearMaMultiplierService(CoinglassAPIBase):
    """Service for 2-Year MA Multiplier indicator"""
    
    def fetch_data(self) -> Dict[str, Any]:
        """Get 2-Year MA Multiplier indicator data"""
        endpoint_suffix = "/indicators/two-year-ma-multiplier"
        return self._make_request_with_prefix(endpoint_suffix)


class PiCycleTopService(CoinglassAPIBase):
    """Service for Pi Cycle Top indicator"""
    
    def fetch_data(self) -> Dict[str, Any]:
        """Get Pi Cycle Top indicator data"""
        endpoint_suffix = "/indicators/pi-cycle-top"
        return self._make_request_with_prefix(endpoint_suffix)


class RainbowChartService(CoinglassAPIBase):
    """Service for Rainbow Chart indicator"""
    
    def fetch_data(self) -> Dict[str, Any]:
        """Get Bitcoin Rainbow Chart data"""
        endpoint_suffix = "/indicators/rainbow-chart"
        return self._make_request_with_prefix(endpoint_suffix)


class ReserveRiskService(CoinglassAPIBase):
    """Service for Reserve Risk indicator"""
    
    def fetch_data(self) -> Dict[str, Any]:
        """Get Reserve Risk indicator data"""
        endpoint_suffix = "/indicators/reserve-risk"
        return self._make_request_with_prefix(endpoint_suffix)


class MvrService(CoinglassAPIBase):
    """Service for MVR (Market Value Ratio) indicator"""
    
    def fetch_data(self) -> Dict[str, Any]:
        """Get MVR indicator data"""
        endpoint_suffix = "/indicators/mvr"
        return self._make_request_with_prefix(endpoint_suffix)


class CoinbaseProPremiumService(CoinglassAPIBase):
    """Service for Coinbase Pro Premium indicator"""
    
    def fetch_data(self) -> Dict[str, Any]:
        """Get Coinbase Pro Premium indicator data"""
        endpoint_suffix = "/indicators/coinbase-pro-premium"
        return self._make_request_with_prefix(endpoint_suffix)


class BinanceBtcUsdtPremiumService(CoinglassAPIBase):
    """Service for Binance BTC/USDT Premium indicator"""
    
    def fetch_data(self) -> Dict[str, Any]:
        """Get Binance BTC/USDT Premium indicator data"""
        endpoint_suffix = "/indicators/binance-btc-usdt-premium"
        return self._make_request_with_prefix(endpoint_suffix)


class BinanceBusdUsdtPremiumService(CoinglassAPIBase):
    """Service for Binance BUSD/USDT Premium indicator"""
    
    def fetch_data(self) -> Dict[str, Any]:
        """Get Binance BUSD/USDT Premium indicator data"""
        endpoint_suffix = "/indicators/binance-busd-usdt-premium"
        return self._make_request_with_prefix(endpoint_suffix)


class TopTradersSentimentService(CoinglassAPIBase):
    """Service for Top Traders Sentiment indicator"""
    
    def fetch_data(self, symbol: str = "BTC") -> Dict[str, Any]:
        """Get Top Traders Sentiment indicator data
        
        Args:
            symbol: Cryptocurrency symbol (default: BTC)
        """
        endpoint_suffix = "/indicators/top-traders-sentiment"
        params = {"symbol": symbol}
        return self._make_request_with_prefix(endpoint_suffix, params)


class RsiIndicatorService(CoinglassAPIBase):
    """Service for RSI indicator"""
    
    def fetch_data(self, symbol: str = "BTC", timeframe: str = "1h") -> Dict[str, Any]:
        """Get RSI indicator data
        
        Args:
            symbol: Cryptocurrency symbol (default: BTC)
            timeframe: Time frame (default: 1h)
        """
        endpoint_suffix = "/indicators/rsi"
        params = {"symbol": symbol, "timeframe": timeframe}
        return self._make_request_with_prefix(endpoint_suffix, params)


class StockToFlowService(CoinglassAPIBase):
    """Service for Stock-to-Flow model"""
    
    def fetch_data(self) -> Dict[str, Any]:
        """Get Stock-to-Flow model data for Bitcoin"""
        endpoint_suffix = "/indicators/stock-to-flow"
        return self._make_request_with_prefix(endpoint_suffix)


class PuellMultipleService(CoinglassAPIBase):
    """Service for Puell Multiple indicator"""
    
    def fetch_data(self) -> Dict[str, Any]:
        """Get Puell Multiple indicator data"""
        endpoint_suffix = "/indicators/puell-multiple"
        return self._make_request_with_prefix(endpoint_suffix)


class NvtRatioService(CoinglassAPIBase):
    """Service for NVT Ratio indicator"""
    
    def fetch_data(self) -> Dict[str, Any]:
        """Get NVT (Network Value to Transactions) Ratio data"""
        endpoint_suffix = "/indicators/nvt-ratio"
        return self._make_request_with_prefix(endpoint_suffix)


class MarketCapToThermocapRatioService(CoinglassAPIBase):
    """Service for Market Cap to Thermocap Ratio"""
    
    def fetch_data(self) -> Dict[str, Any]:
        """Get Market Cap to Thermocap Ratio data"""
        endpoint_suffix = "/indicators/marketcap-thermocap-ratio"
        return self._make_request_with_prefix(endpoint_suffix)