from typing import List, Dict, Any, Optional
from services.market_data import (
    CoinsMarketsService,
    PairsMarketsService,
    CoinsPriceChangeService,
    ExchangeRankService
)
from services.open_interest import (
    OpenInterestExchangeListService,
    AggregatedOpenInterestHistoryService
)
from services.price_data import PriceHistoryService


class MarketDataManager:
    """Manager class for comprehensive market data operations"""
    
    def __init__(self):
        self.coins_markets_service = CoinsMarketsService()
        self.pairs_markets_service = PairsMarketsService()
        self.price_change_service = CoinsPriceChangeService()
        self.exchange_rank_service = ExchangeRankService()
        self.oi_exchange_service = OpenInterestExchangeListService()
        self.oi_history_service = AggregatedOpenInterestHistoryService()
        self.price_history_service = PriceHistoryService()
    
    def get_market_overview(self, top_n: int = 10) -> Dict[str, Any]:
        """
        Get comprehensive market overview for top coins
        
        :param top_n: Number of top coins to include
        :return: Market overview data
        """
        overview = {}
        
        # Get coins market data
        try:
            coins_data = self.coins_markets_service.fetch_data()
            if coins_data.get("code") == "0":
                all_coins = coins_data.get("data", [])
                # Sort by market cap and take top N
                sorted_coins = sorted(
                    all_coins, 
                    key=lambda x: x.get("market_cap_usd", 0), 
                    reverse=True
                )[:top_n]
                
                overview["top_coins"] = sorted_coins
                overview["total_market_metrics"] = self._calculate_market_metrics(sorted_coins)
        except Exception as e:
            overview["error"] = str(e)
        
        # Get exchange rankings
        try:
            exchange_data = self.exchange_rank_service.fetch_data()
            if exchange_data.get("code") == "0":
                overview["exchange_rankings"] = exchange_data.get("data", [])
        except Exception as e:
            overview["exchange_rankings_error"] = str(e)
        
        return overview
    
    def get_coin_analysis(self, symbol: str) -> Dict[str, Any]:
        """
        Get comprehensive analysis for a specific coin
        
        :param symbol: Cryptocurrency symbol (e.g., 'BTC')
        :return: Detailed coin analysis
        """
        analysis = {"symbol": symbol}
        
        # Get current market data
        try:
            coins_data = self.coins_markets_service.fetch_data()
            if coins_data.get("code") == "0":
                coin_data = next(
                    (coin for coin in coins_data.get("data", []) if coin.get("symbol") == symbol),
                    None
                )
                if coin_data:
                    analysis["current_metrics"] = coin_data
        except Exception as e:
            analysis["metrics_error"] = str(e)
        
        # Get price change data
        try:
            price_change_data = self.price_change_service.fetch_data()
            if price_change_data.get("code") == "0":
                coin_price_change = next(
                    (coin for coin in price_change_data.get("data", []) if coin.get("symbol") == symbol),
                    None
                )
                if coin_price_change:
                    analysis["price_changes"] = coin_price_change
        except Exception as e:
            analysis["price_change_error"] = str(e)
        
        # Get open interest distribution
        try:
            oi_data = self.oi_exchange_service.fetch_data(symbol=symbol)
            if oi_data.get("code") == "0":
                analysis["open_interest_distribution"] = oi_data.get("data", {})
        except Exception as e:
            analysis["oi_distribution_error"] = str(e)
        
        # Get recent price history
        try:
            price_history = self.price_history_service.fetch_data(symbol=symbol, interval="1h")
            if price_history.get("code") == "0":
                history_data = price_history.get("data", [])
                if history_data:
                    # Calculate some basic statistics
                    prices = [float(candle.get("close", 0)) for candle in history_data[-24:]]  # Last 24 hours
                    if prices:
                        analysis["price_statistics_24h"] = {
                            "high": max(prices),
                            "low": min(prices),
                            "average": sum(prices) / len(prices),
                            "volatility": self._calculate_volatility(prices)
                        }
        except Exception as e:
            analysis["price_history_error"] = str(e)
        
        return analysis
    
    def get_pairs_performance(self, exchange: str = "Binance", top_n: int = 20) -> List[Dict[str, Any]]:
        """
        Get performance metrics for top trading pairs on an exchange
        
        :param exchange: Exchange name
        :param top_n: Number of top pairs to return
        :return: List of top performing pairs
        """
        try:
            pairs_data = self.pairs_markets_service.fetch_data()
            if pairs_data.get("code") == "0":
                all_pairs = pairs_data.get("data", [])
                
                # Filter by exchange
                exchange_pairs = [
                    pair for pair in all_pairs 
                    if pair.get("exchange_name", "").lower() == exchange.lower()
                ]
                
                # Sort by volume and take top N
                sorted_pairs = sorted(
                    exchange_pairs,
                    key=lambda x: x.get("volume_usd", 0),
                    reverse=True
                )[:top_n]
                
                return sorted_pairs
            else:
                raise ValueError(f"Error fetching pairs data: {pairs_data.get('msg')}")
        except Exception as e:
            return [{"error": str(e)}]
    
    def compare_exchanges(self, symbol: str = "BTC") -> Dict[str, Any]:
        """
        Compare metrics across exchanges for a given coin
        
        :param symbol: Cryptocurrency symbol
        :return: Exchange comparison data
        """
        comparison = {"symbol": symbol}
        
        # Get pairs data for all exchanges
        try:
            pairs_data = self.pairs_markets_service.fetch_data()
            if pairs_data.get("code") == "0":
                all_pairs = pairs_data.get("data", [])
                
                # Filter pairs for the given symbol
                symbol_pairs = [
                    pair for pair in all_pairs
                    if pair.get("symbol", "").startswith(f"{symbol}/")
                ]
                
                # Group by exchange
                exchange_metrics = {}
                for pair in symbol_pairs:
                    exchange = pair.get("exchange_name", "Unknown")
                    if exchange not in exchange_metrics:
                        exchange_metrics[exchange] = {
                            "total_volume_usd": 0,
                            "total_open_interest_usd": 0,
                            "pairs_count": 0,
                            "avg_funding_rate": 0,
                            "funding_rates": []
                        }
                    
                    metrics = exchange_metrics[exchange]
                    metrics["total_volume_usd"] += pair.get("volume_usd", 0)
                    metrics["total_open_interest_usd"] += pair.get("open_interest_usd", 0)
                    metrics["pairs_count"] += 1
                    
                    funding_rate = pair.get("funding_rate", 0)
                    if funding_rate:
                        metrics["funding_rates"].append(funding_rate)
                
                # Calculate average funding rates
                for exchange, metrics in exchange_metrics.items():
                    if metrics["funding_rates"]:
                        metrics["avg_funding_rate"] = sum(metrics["funding_rates"]) / len(metrics["funding_rates"])
                    del metrics["funding_rates"]  # Remove the list, keep only average
                
                comparison["exchanges"] = exchange_metrics
                
                # Rank exchanges by volume
                volume_ranking = sorted(
                    [(ex, data["total_volume_usd"]) for ex, data in exchange_metrics.items()],
                    key=lambda x: x[1],
                    reverse=True
                )
                comparison["volume_ranking"] = [{"exchange": ex, "volume_usd": vol} for ex, vol in volume_ranking]
                
        except Exception as e:
            comparison["error"] = str(e)
        
        return comparison
    
    def _calculate_market_metrics(self, coins: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Calculate aggregate market metrics"""
        if not coins:
            return {}
        
        total_market_cap = sum(coin.get("market_cap_usd", 0) for coin in coins)
        total_volume = sum(coin.get("volume_usd_24h", 0) for coin in coins)
        total_open_interest = sum(coin.get("open_interest_usd", 0) for coin in coins)
        
        avg_funding_rate = sum(coin.get("avg_funding_rate_by_oi", 0) for coin in coins) / len(coins)
        avg_price_change = sum(coin.get("price_change_percent_24h", 0) for coin in coins) / len(coins)
        
        return {
            "total_market_cap_usd": total_market_cap,
            "total_volume_24h_usd": total_volume,
            "total_open_interest_usd": total_open_interest,
            "average_funding_rate": avg_funding_rate,
            "average_price_change_24h": avg_price_change,
            "coins_analyzed": len(coins)
        }
    
    def _calculate_volatility(self, prices: List[float]) -> float:
        """Calculate simple volatility as percentage"""
        if len(prices) < 2:
            return 0
        
        mean = sum(prices) / len(prices)
        variance = sum((x - mean) ** 2 for x in prices) / len(prices)
        std_dev = variance ** 0.5
        
        return (std_dev / mean) * 100 if mean > 0 else 0