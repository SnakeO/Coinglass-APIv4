from typing import Dict, Any, List, Optional
from services.indicators import (
    FearGreedIndexService,
    BitcoinRainbowChartService,
    AHR999Service,
    BitcoinProfitableDaysService,
    PuellMultipleService,
    StockToFlowService,
    BitcoinNetUnrealizedPNLService,
    BitcoinActiveAddressesService,
    CoinbasePremiumIndexService,
    BitfinexMarginLongShortService
)


class IndicatorsManager:
    """Manager class for handling Bitcoin indicators and market metrics"""
    
    def __init__(self):
        self.fear_greed_service = FearGreedIndexService()
        self.rainbow_chart_service = BitcoinRainbowChartService()
        self.ahr999_service = AHR999Service()
        self.profitable_days_service = BitcoinProfitableDaysService()
        self.puell_multiple_service = PuellMultipleService()
        self.stock_to_flow_service = StockToFlowService()
        self.nupl_service = BitcoinNetUnrealizedPNLService()
        self.active_addresses_service = BitcoinActiveAddressesService()
        self.coinbase_premium_service = CoinbasePremiumIndexService()
        self.bitfinex_margin_service = BitfinexMarginLongShortService()
    
    def get_fear_greed_index(self) -> Dict[str, Any]:
        """
        Get the current and historical Fear & Greed Index
        
        :return: Fear & Greed Index data
        """
        data = self.fear_greed_service.fetch_data()
        
        if data.get("code") != "0":
            raise ValueError(f"Error fetching Fear & Greed Index: {data.get('msg')}")
        
        return data.get("data", {})
    
    def get_bitcoin_rainbow_chart(self) -> Dict[str, Any]:
        """
        Get Bitcoin Rainbow Chart data
        
        :return: Rainbow Chart data points
        """
        data = self.rainbow_chart_service.fetch_data()
        
        if data.get("code") != "0":
            raise ValueError(f"Error fetching Rainbow Chart: {data.get('msg')}")
        
        return data.get("data", [])
    
    def get_ahr999_index(self) -> Dict[str, Any]:
        """
        Get AHR999 Index value
        
        :return: AHR999 Index data
        """
        data = self.ahr999_service.fetch_data()
        
        if data.get("code") != "0":
            raise ValueError(f"Error fetching AHR999 Index: {data.get('msg')}")
        
        return data.get("data", {})
    
    def get_market_sentiment_overview(self) -> Dict[str, Any]:
        """
        Get a comprehensive overview of market sentiment indicators
        
        :return: Dictionary containing multiple sentiment indicators
        """
        sentiment_data = {}
        
        # Fear & Greed Index
        try:
            fg_data = self.get_fear_greed_index()
            if isinstance(fg_data, dict) and "data_list" in fg_data:
                latest_value = fg_data["data_list"][-1] if fg_data["data_list"] else None
                sentiment_data["fear_greed_index"] = {
                    "value": latest_value,
                    "classification": self._classify_fear_greed(latest_value)
                }
        except Exception as e:
            sentiment_data["fear_greed_index"] = {"error": str(e)}
        
        # AHR999 Index
        try:
            ahr999_data = self.get_ahr999_index()
            sentiment_data["ahr999_index"] = {
                "value": ahr999_data.get("value"),
                "signal": self._interpret_ahr999(ahr999_data.get("value"))
            }
        except Exception as e:
            sentiment_data["ahr999_index"] = {"error": str(e)}
        
        # Coinbase Premium
        try:
            premium_data = self.coinbase_premium_service.fetch_data()
            if premium_data.get("code") == "0" and premium_data.get("data"):
                latest_premium = premium_data["data"][-1] if premium_data["data"] else {}
                sentiment_data["coinbase_premium"] = {
                    "value": latest_premium.get("premium_percent"),
                    "interpretation": self._interpret_coinbase_premium(latest_premium.get("premium_percent"))
                }
        except Exception as e:
            sentiment_data["coinbase_premium"] = {"error": str(e)}
        
        return sentiment_data
    
    def get_on_chain_metrics(self) -> Dict[str, Any]:
        """
        Get comprehensive on-chain metrics
        
        :return: Dictionary containing various on-chain metrics
        """
        metrics = {}
        
        # Bitcoin Profitable Days
        try:
            profitable_data = self.profitable_days_service.fetch_data()
            if profitable_data.get("code") == "0":
                metrics["profitable_days_percent"] = profitable_data.get("data", {}).get("percent_profitable_days")
        except Exception as e:
            metrics["profitable_days_percent"] = {"error": str(e)}
        
        # NUPL (Net Unrealized Profit/Loss)
        try:
            nupl_data = self.nupl_service.fetch_data()
            if nupl_data.get("code") == "0" and nupl_data.get("data"):
                latest_nupl = nupl_data["data"][-1] if isinstance(nupl_data["data"], list) else nupl_data["data"]
                metrics["nupl"] = {
                    "value": latest_nupl,
                    "market_phase": self._classify_nupl(latest_nupl)
                }
        except Exception as e:
            metrics["nupl"] = {"error": str(e)}
        
        # Active Addresses
        try:
            active_addr_data = self.active_addresses_service.fetch_data()
            if active_addr_data.get("code") == "0" and active_addr_data.get("data"):
                metrics["active_addresses"] = active_addr_data["data"]
        except Exception as e:
            metrics["active_addresses"] = {"error": str(e)}
        
        return metrics
    
    def get_valuation_metrics(self) -> Dict[str, Any]:
        """
        Get Bitcoin valuation metrics
        
        :return: Dictionary containing valuation indicators
        """
        valuation = {}
        
        # Puell Multiple
        try:
            puell_data = self.puell_multiple_service.fetch_data()
            if puell_data.get("code") == "0":
                valuation["puell_multiple"] = puell_data.get("data", {})
        except Exception as e:
            valuation["puell_multiple"] = {"error": str(e)}
        
        # Stock-to-Flow
        try:
            s2f_data = self.stock_to_flow_service.fetch_data()
            if s2f_data.get("code") == "0":
                valuation["stock_to_flow"] = s2f_data.get("data", {})
        except Exception as e:
            valuation["stock_to_flow"] = {"error": str(e)}
        
        return valuation
    
    def _classify_fear_greed(self, value: Optional[float]) -> str:
        """Classify Fear & Greed Index value"""
        if value is None:
            return "unknown"
        if value < 20:
            return "extreme_fear"
        elif value < 40:
            return "fear"
        elif value < 60:
            return "neutral"
        elif value < 80:
            return "greed"
        else:
            return "extreme_greed"
    
    def _interpret_ahr999(self, value: Optional[float]) -> str:
        """Interpret AHR999 Index value"""
        if value is None:
            return "unknown"
        if value < 0.45:
            return "bottom_fishing_zone"
        elif value < 1.2:
            return "regular_investment_zone"
        else:
            return "wait_zone"
    
    def _interpret_coinbase_premium(self, premium: Optional[float]) -> str:
        """Interpret Coinbase Premium"""
        if premium is None:
            return "unknown"
        if premium > 0.5:
            return "strong_institutional_buying"
        elif premium > 0:
            return "institutional_buying"
        elif premium < -0.5:
            return "strong_institutional_selling"
        else:
            return "institutional_selling"
    
    def _classify_nupl(self, value: Optional[float]) -> str:
        """Classify NUPL market phase"""
        if value is None:
            return "unknown"
        if value < 0:
            return "capitulation"
        elif value < 0.25:
            return "hope_fear"
        elif value < 0.5:
            return "optimism_anxiety"
        elif value < 0.75:
            return "belief_denial"
        else:
            return "euphoria_greed"