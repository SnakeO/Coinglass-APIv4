#!/usr/bin/env python3
"""Manager for extended futures services"""

from typing import Dict, Any, Optional
import pandas as pd
from ..services.futures_extended import (
    FuturesVolumeService,
    FuturesOpenInterestAggregatedService,
    FuturesBasisService,
    FuturesGlobalAverageService,
    FuturesTopAccountRatioService,
    FuturesTopPositionRatioService,
    FuturesActiveBuyingSelling12HService,
    FuturesActiveBuyingSelling24HService,
    FuturesBubbleColorService,
    FuturesStablesFundingRatesService
)


class FuturesExtendedManager:
    """Manager for extended futures data operations"""
    
    def __init__(self):
        self.volume_service = FuturesVolumeService()
        self.oi_aggregated_service = FuturesOpenInterestAggregatedService()
        self.basis_service = FuturesBasisService()
        self.global_average_service = FuturesGlobalAverageService()
        self.top_account_ratio_service = FuturesTopAccountRatioService()
        self.top_position_ratio_service = FuturesTopPositionRatioService()
        self.active_bs_12h_service = FuturesActiveBuyingSelling12HService()
        self.active_bs_24h_service = FuturesActiveBuyingSelling24HService()
        self.bubble_color_service = FuturesBubbleColorService()
        self.stables_funding_service = FuturesStablesFundingRatesService()
    
    def get_futures_volume(self, symbol: str = "BTC", exchange: Optional[str] = None) -> Dict[str, Any]:
        """Get futures volume data"""
        try:
            data = self.volume_service.fetch_data(symbol, exchange)
            if data.get("code") == "0":
                return {"success": True, "data": data.get("data", [])}
            return {"success": False, "error": data.get("msg", "Failed to fetch futures volume")}
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def get_aggregated_open_interest(self, symbol: str = "BTC") -> Dict[str, Any]:
        """Get aggregated futures open interest"""
        try:
            data = self.oi_aggregated_service.fetch_data(symbol)
            if data.get("code") == "0":
                return {"success": True, "data": data.get("data", [])}
            return {"success": False, "error": data.get("msg", "Failed to fetch aggregated OI")}
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def get_futures_basis(self, symbol: str = "BTC", exchange: Optional[str] = None) -> Dict[str, Any]:
        """Get futures basis data"""
        try:
            data = self.basis_service.fetch_data(symbol, exchange)
            if data.get("code") == "0":
                return {"success": True, "data": data.get("data", [])}
            return {"success": False, "error": data.get("msg", "Failed to fetch futures basis")}
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def get_global_average_price(self, symbol: str = "BTC") -> Dict[str, Any]:
        """Get futures global average price"""
        try:
            data = self.global_average_service.fetch_data(symbol)
            if data.get("code") == "0":
                return {"success": True, "data": data.get("data", [])}
            return {"success": False, "error": data.get("msg", "Failed to fetch global average")}
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def get_top_account_ratio(self, symbol: str = "BTC", exchange: str = "Binance") -> Dict[str, Any]:
        """Get futures top account ratio"""
        try:
            data = self.top_account_ratio_service.fetch_data(symbol, exchange)
            if data.get("code") == "0":
                return {"success": True, "data": data.get("data", [])}
            return {"success": False, "error": data.get("msg", "Failed to fetch top account ratio")}
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def get_top_position_ratio(self, symbol: str = "BTC", exchange: str = "Binance") -> Dict[str, Any]:
        """Get futures top position ratio"""
        try:
            data = self.top_position_ratio_service.fetch_data(symbol, exchange)
            if data.get("code") == "0":
                return {"success": True, "data": data.get("data", [])}
            return {"success": False, "error": data.get("msg", "Failed to fetch top position ratio")}
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def get_active_buying_selling_12h(self, symbol: str = "BTC", exchange: Optional[str] = None) -> Dict[str, Any]:
        """Get 12H active buying/selling data"""
        try:
            data = self.active_bs_12h_service.fetch_data(symbol, exchange)
            if data.get("code") == "0":
                return {"success": True, "data": data.get("data", [])}
            return {"success": False, "error": data.get("msg", "Failed to fetch 12H data")}
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def get_active_buying_selling_24h(self, symbol: str = "BTC", exchange: Optional[str] = None) -> Dict[str, Any]:
        """Get 24H active buying/selling data"""
        try:
            data = self.active_bs_24h_service.fetch_data(symbol, exchange)
            if data.get("code") == "0":
                return {"success": True, "data": data.get("data", [])}
            return {"success": False, "error": data.get("msg", "Failed to fetch 24H data")}
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def get_bubble_color_analysis(self, symbol: str = "BTC", exchange: Optional[str] = None) -> Dict[str, Any]:
        """Get bubble color volatility/volume analysis"""
        try:
            data = self.bubble_color_service.fetch_data(symbol, exchange)
            if data.get("code") == "0":
                return {"success": True, "data": data.get("data", [])}
            return {"success": False, "error": data.get("msg", "Failed to fetch bubble color data")}
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def get_stables_funding_rates(self, stablecoin: str = "USDT") -> Dict[str, Any]:
        """Get stablecoins funding rates"""
        try:
            data = self.stables_funding_service.fetch_data(stablecoin)
            if data.get("code") == "0":
                return {"success": True, "data": data.get("data", [])}
            return {"success": False, "error": data.get("msg", "Failed to fetch stables funding")}
        except Exception as e:
            return {"success": False, "error": str(e)}