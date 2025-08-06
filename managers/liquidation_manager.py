from typing import List, Dict, Any, Optional
from services.liquidation import (
    LiquidationHistoryService,
    AggregatedLiquidationHistoryService,
    AggregatedLiquidationHeatmapModel2Service,
    LiquidationOrderService,
    LiquidationCoinListService,
    LiquidationExchangeListService
)


class LiquidationManager:
    """Manager class for handling liquidation data operations"""
    
    def __init__(self):
        self.history_service = LiquidationHistoryService()
        self.aggregated_history_service = AggregatedLiquidationHistoryService()
        self.heatmap_service = AggregatedLiquidationHeatmapModel2Service()
        self.order_service = LiquidationOrderService()
        self.coin_list_service = LiquidationCoinListService()
        self.exchange_list_service = LiquidationExchangeListService()
    
    def get_liquidation_history(self, symbol: str, interval: str = "1h") -> Dict[str, Any]:
        """
        Get liquidation history for a specific symbol
        
        :param symbol: Cryptocurrency symbol (e.g., 'BTC')
        :param interval: Time interval (e.g., '1h', '4h', '1d')
        :return: Liquidation history data
        """
        data = self.history_service.fetch_data(symbol=symbol, interval=interval)
        
        if data.get("code") != "0":
            raise ValueError(f"Error fetching liquidation history: {data.get('msg')}")
        
        return data.get("data", [])
    
    def get_aggregated_liquidation_history(self, symbol: str, interval: str = "1h") -> Dict[str, Any]:
        """
        Get aggregated liquidation history across all exchanges
        
        :param symbol: Cryptocurrency symbol (e.g., 'BTC')
        :param interval: Time interval (e.g., '1h', '4h', '1d')
        :return: Aggregated liquidation history data
        """
        data = self.aggregated_history_service.fetch_data(symbol=symbol, interval=interval)
        
        if data.get("code") != "0":
            raise ValueError(f"Error fetching aggregated liquidation history: {data.get('msg')}")
        
        return data.get("data", [])
    
    def get_liquidation_heatmap(self, symbol: str) -> Dict[str, Any]:
        """
        Get liquidation heatmap data for visualization
        
        :param symbol: Cryptocurrency symbol (e.g., 'BTC')
        :return: Liquidation heatmap data
        """
        data = self.heatmap_service.fetch_data(symbol=symbol)
        
        if data.get("code") != "0":
            raise ValueError(f"Error fetching liquidation heatmap: {data.get('msg')}")
        
        return data.get("data", {})
    
    def get_large_liquidation_orders(self) -> List[Dict[str, Any]]:
        """
        Get recent large liquidation orders
        
        :return: List of large liquidation orders
        """
        data = self.order_service.fetch_data()
        
        if data.get("code") != "0":
            raise ValueError(f"Error fetching liquidation orders: {data.get('msg')}")
        
        return data.get("data", [])
    
    def get_supported_coins(self) -> List[str]:
        """
        Get list of coins with available liquidation data
        
        :return: List of supported coin symbols
        """
        data = self.coin_list_service.fetch_data()
        
        if data.get("code") != "0":
            raise ValueError(f"Error fetching supported coins: {data.get('msg')}")
        
        return data.get("data", [])
    
    def get_supported_exchanges(self) -> List[str]:
        """
        Get list of exchanges with liquidation data
        
        :return: List of supported exchange names
        """
        data = self.exchange_list_service.fetch_data()
        
        if data.get("code") != "0":
            raise ValueError(f"Error fetching supported exchanges: {data.get('msg')}")
        
        return data.get("data", [])
    
    def analyze_liquidation_trends(self, symbol: str, interval: str = "1h", periods: int = 24) -> Dict[str, Any]:
        """
        Analyze liquidation trends for a given symbol
        
        :param symbol: Cryptocurrency symbol
        :param interval: Time interval
        :param periods: Number of periods to analyze
        :return: Analysis results including totals, averages, and trends
        """
        history = self.get_aggregated_liquidation_history(symbol, interval)
        
        if not history:
            return {"error": "No data available"}
        
        # Take only the requested number of periods
        recent_data = history[-periods:] if len(history) > periods else history
        
        total_long_liquidations = sum(float(d.get("long_liquidation_usd", 0)) for d in recent_data)
        total_short_liquidations = sum(float(d.get("short_liquidation_usd", 0)) for d in recent_data)
        total_liquidations = total_long_liquidations + total_short_liquidations
        
        avg_long_liquidations = total_long_liquidations / len(recent_data) if recent_data else 0
        avg_short_liquidations = total_short_liquidations / len(recent_data) if recent_data else 0
        
        # Calculate trend (comparing first half to second half)
        mid_point = len(recent_data) // 2
        if mid_point > 0:
            first_half_total = sum(
                float(d.get("long_liquidation_usd", 0)) + float(d.get("short_liquidation_usd", 0))
                for d in recent_data[:mid_point]
            )
            second_half_total = sum(
                float(d.get("long_liquidation_usd", 0)) + float(d.get("short_liquidation_usd", 0))
                for d in recent_data[mid_point:]
            )
            trend = "increasing" if second_half_total > first_half_total else "decreasing"
        else:
            trend = "insufficient data"
        
        return {
            "symbol": symbol,
            "interval": interval,
            "periods_analyzed": len(recent_data),
            "total_liquidations_usd": total_liquidations,
            "total_long_liquidations_usd": total_long_liquidations,
            "total_short_liquidations_usd": total_short_liquidations,
            "average_long_liquidations_usd": avg_long_liquidations,
            "average_short_liquidations_usd": avg_short_liquidations,
            "long_short_ratio": total_long_liquidations / total_short_liquidations if total_short_liquidations > 0 else 0,
            "trend": trend,
            "latest_data": recent_data[-1] if recent_data else None
        }