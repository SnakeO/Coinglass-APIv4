from typing import Any, Dict, Optional
from services.base import CoinglassAPIBase


class IndicatorsBaseService(CoinglassAPIBase):
    """Base service for indicator-related endpoints"""
    
    def _make_index_request(self, endpoint: str, params: dict | None = None) -> dict:
        return self._make_request(endpoint, params)


class FearGreedIndexService(IndicatorsBaseService):
    """Service for fetching the historical Crypto Fear & Greed Index"""
    
    def fetch_data(self) -> Dict[str, Any]:
        endpoint = "/index/fear-greed-history"
        return self._make_index_request(endpoint)


class OptionVsFuturesOIRatioService(IndicatorsBaseService):
    """Service for fetching Options/Futures Open Interest Ratio"""
    
    def fetch_data(self) -> Dict[str, Any]:
        endpoint = "/index/option-vs-futures-oi-ratio"
        return self._make_index_request(endpoint)


class BitcoinVsGlobalM2GrowthService(IndicatorsBaseService):
    """Service for fetching Bitcoin vs Global M2 money supply growth"""
    
    def fetch_data(self) -> Dict[str, Any]:
        endpoint = "/index/bitcoin-vs-global-m2-growth"
        return self._make_index_request(endpoint)


class BitcoinVsUSM2GrowthService(IndicatorsBaseService):
    """Service for fetching Bitcoin vs US M2 money supply growth"""
    
    def fetch_data(self) -> Dict[str, Any]:
        endpoint = "/index/bitcoin-vs-us-m2-growth"
        return self._make_index_request(endpoint)


class AHR999Service(IndicatorsBaseService):
    """Service for fetching AHR999 indicator"""
    
    def fetch_data(self) -> Dict[str, Any]:
        endpoint = "/index/ahr999"
        return self._make_index_request(endpoint)


class TwoYearMAMultiplierService(IndicatorsBaseService):
    """Service for fetching Two-Year Moving Average Multiplier"""
    
    def fetch_data(self) -> Dict[str, Any]:
        endpoint = "/index/2-year-ma-multiplier"
        return self._make_index_request(endpoint)


class TwoHundredWeekMAHeatmapService(IndicatorsBaseService):
    """Service for fetching 200-Week Moving Average Heatmap"""
    
    def fetch_data(self) -> Dict[str, Any]:
        endpoint = "/index/200-week-moving-avg-heatmap"
        return self._make_index_request(endpoint)


class AltcoinSeasonIndexService(IndicatorsBaseService):
    """Service for fetching Altcoin Season Index"""
    
    def fetch_data(self) -> Dict[str, Any]:
        endpoint = "/index/altcoin-season-index"
        return self._make_index_request(endpoint)


class BitcoinShortTermHolderSOPRService(IndicatorsBaseService):
    """Service for fetching Bitcoin Short-Term Holder SOPR"""
    
    def fetch_data(self) -> Dict[str, Any]:
        endpoint = "/index/bitcoin-short-term-holder-sopr"
        return self._make_index_request(endpoint)


class BitcoinLongTermHolderSOPRService(IndicatorsBaseService):
    """Service for fetching Bitcoin Long-Term Holder SOPR"""
    
    def fetch_data(self) -> Dict[str, Any]:
        endpoint = "/index/bitcoin-long-term-holder-sopr"
        return self._make_index_request(endpoint)


class BitcoinShortTermHolderRealizedPriceService(IndicatorsBaseService):
    """Service for fetching Bitcoin Short-Term Holder Realized Price"""
    
    def fetch_data(self) -> Dict[str, Any]:
        endpoint = "/index/bitcoin-short-term-holder-realized-price"
        return self._make_index_request(endpoint)


class BitcoinLongTermHolderRealizedPriceService(IndicatorsBaseService):
    """Service for fetching Bitcoin Long-Term Holder Realized Price"""
    
    def fetch_data(self) -> Dict[str, Any]:
        endpoint = "/index/bitcoin-long-term-holder-realized-price"
        return self._make_index_request(endpoint)


class BitcoinShortTermHolderSupplyService(IndicatorsBaseService):
    """Service for fetching Bitcoin Short-Term Holder Supply"""
    
    def fetch_data(self) -> Dict[str, Any]:
        endpoint = "/index/bitcoin-short-term-holder-supply"
        return self._make_index_request(endpoint)


class BitcoinLongTermHolderSupplyService(IndicatorsBaseService):
    """Service for fetching Bitcoin Long-Term Holder Supply"""
    
    def fetch_data(self) -> Dict[str, Any]:
        endpoint = "/index/bitcoin-long-term-holder-supply"
        return self._make_index_request(endpoint)


class BitcoinRHODLRatioService(IndicatorsBaseService):
    """Service for fetching Bitcoin RHODL Ratio"""
    
    def fetch_data(self) -> Dict[str, Any]:
        endpoint = "/index/bitcoin-rhodl-ratio"
        return self._make_index_request(endpoint)


class BitcoinReserveRiskService(IndicatorsBaseService):
    """Service for fetching Bitcoin Reserve Risk"""
    
    def fetch_data(self) -> Dict[str, Any]:
        endpoint = "/index/bitcoin-reserve-risk"
        return self._make_index_request(endpoint)


class BitcoinActiveAddressesService(IndicatorsBaseService):
    """Service for fetching Bitcoin Active Addresses"""
    
    def fetch_data(self) -> Dict[str, Any]:
        endpoint = "/index/bitcoin-active-addresses"
        return self._make_index_request(endpoint)


class BitcoinNewAddressesService(IndicatorsBaseService):
    """Service for fetching Bitcoin New Addresses"""
    
    def fetch_data(self) -> Dict[str, Any]:
        endpoint = "/index/bitcoin-new-addresses"
        return self._make_index_request(endpoint)


class BitcoinNetUnrealizedPNLService(IndicatorsBaseService):
    """Service for fetching Bitcoin Net Unrealized Profit/Loss"""
    
    def fetch_data(self) -> Dict[str, Any]:
        endpoint = "/index/bitcoin-net-unrealized-pnl"
        return self._make_index_request(endpoint)


class BTCCorrelationsService(IndicatorsBaseService):
    """Service for fetching BTC correlations with other assets"""
    
    def fetch_data(self) -> Dict[str, Any]:
        endpoint = "/index/btc-correlations"
        return self._make_index_request(endpoint)


class BitcoinMacroOscillatorService(IndicatorsBaseService):
    """Service for fetching Bitcoin Macro Oscillator"""
    
    def fetch_data(self) -> Dict[str, Any]:
        endpoint = "/index/bitcoin-macro-oscillator"
        return self._make_index_request(endpoint)


class BitcoinRainbowChartService(IndicatorsBaseService):
    """Service for fetching Bitcoin Rainbow Chart data"""
    
    def fetch_data(self) -> Dict[str, Any]:
        endpoint = "/bitcoin-rainbow-chart"
        return self._make_request(endpoint)


class BitcoinProfitableDaysService(IndicatorsBaseService):
    """Service for fetching Bitcoin Profitable Days percentage"""
    
    def fetch_data(self) -> Dict[str, Any]:
        endpoint = "/bitcoin-profitable-days"
        return self._make_request(endpoint)


class PuellMultipleService(IndicatorsBaseService):
    """Service for fetching Puell Multiple"""
    
    def fetch_data(self) -> Dict[str, Any]:
        endpoint = "/puell-multiple"
        return self._make_request(endpoint)


class StockToFlowService(IndicatorsBaseService):
    """Service for fetching Stock-to-Flow model data"""
    
    def fetch_data(self) -> Dict[str, Any]:
        endpoint = "/stock-to-flow"
        return self._make_request(endpoint)


class PiCycleTopIndicatorService(IndicatorsBaseService):
    """Service for fetching Pi Cycle Top Indicator"""
    
    def fetch_data(self) -> Dict[str, Any]:
        endpoint = "/pi-cycle-top-indicator"
        return self._make_request(endpoint)


class GoldenRatioMultiplierService(IndicatorsBaseService):
    """Service for fetching Golden Ratio Multiplier"""
    
    def fetch_data(self) -> Dict[str, Any]:
        endpoint = "/golden-ratio-multiplier"
        return self._make_request(endpoint)


class BullMarketPeakIndicatorService(IndicatorsBaseService):
    """Service for fetching Bull Market Peak Indicators"""
    
    def fetch_data(self) -> Dict[str, Any]:
        endpoint = "/bull-market-peak-indicator"
        return self._make_request(endpoint)


class CoinbasePremiumIndexService(IndicatorsBaseService):
    """Service for fetching Coinbase Premium Index"""
    
    def fetch_data(self, interval: Optional[str] = None) -> Dict[str, Any]:
        endpoint = "/coinbase-premium-index"
        params = {"interval": interval} if interval else None
        return self._make_request(endpoint, params)


class BitfinexMarginLongShortService(IndicatorsBaseService):
    """Service for fetching Bitfinex margin long vs short positions"""
    
    def fetch_data(self) -> Dict[str, Any]:
        endpoint = "/bitfinex-margin-long-short"
        return self._make_request(endpoint)


class BorrowInterestRateHistoryService(IndicatorsBaseService):
    """Service for fetching borrow interest rate history"""
    
    def fetch_data(self) -> Dict[str, Any]:
        endpoint = "/borrow-interest-rate/history"
        return self._make_request(endpoint)