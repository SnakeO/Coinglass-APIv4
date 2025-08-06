from managers.base import FundingRateManager, TopPairsManager
from managers.liquidation_manager import LiquidationManager
from managers.indicators_manager import IndicatorsManager
from managers.market_data_manager import MarketDataManager
from services.funding_rates import ExchangeListService
import json


def print_section(title):
    """Print a formatted section header"""
    print(f"\n{'='*60}")
    print(f"{title:^60}")
    print('='*60)


def demonstrate_basic_usage():
    """Demonstrate basic API usage with top pairs and funding rates"""
    print_section("Basic Usage - Top Pairs & Funding Rates")
    
    # Get top trading pairs
    top_pairs_manager = TopPairsManager()
    top_pairs = top_pairs_manager.get_top_pairs(top_n=3)
    print(f"\nTop 3 Trading Pairs: {', '.join(top_pairs)}")
    
    # Get funding rates
    funding_rate_manager = FundingRateManager(Service=ExchangeListService)
    funding_rates = funding_rate_manager.get_funding_rate(top_pairs[:1])
    
    if funding_rates:
        pair = list(funding_rates.keys())[0]
        print(f"\nFunding Rates for {pair}:")
        for exchange, data in list(funding_rates[pair].items())[:5]:
            print(f"  {exchange}: {data['funding_rate']:.4f}%")


def demonstrate_market_analysis():
    """Demonstrate market analysis capabilities"""
    print_section("Market Analysis")
    
    market_manager = MarketDataManager()
    
    # Get market overview
    try:
        overview = market_manager.get_market_overview(top_n=5)
        if "total_market_metrics" in overview:
            metrics = overview["total_market_metrics"]
            print(f"\nMarket Overview (Top 5 Coins):")
            print(f"  Total Market Cap: ${metrics['total_market_cap_usd']:,.0f}")
            print(f"  Total 24h Volume: ${metrics['total_volume_24h_usd']:,.0f}")
            print(f"  Average Price Change: {metrics['average_price_change_24h']:.2f}%")
    except Exception as e:
        print(f"Error getting market overview: {e}")
    
    # Analyze Bitcoin
    try:
        btc_analysis = market_manager.get_coin_analysis("BTC")
        if "current_metrics" in btc_analysis:
            print(f"\nBitcoin Analysis:")
            metrics = btc_analysis["current_metrics"]
            print(f"  Price: ${metrics.get('price', 0):,.2f}")
            print(f"  Market Cap: ${metrics.get('market_cap_usd', 0):,.0f}")
            print(f"  24h Volume: ${metrics.get('volume_usd_24h', 0):,.0f}")
    except Exception as e:
        print(f"Error analyzing BTC: {e}")


def demonstrate_liquidation_tracking():
    """Demonstrate liquidation tracking features"""
    print_section("Liquidation Tracking")
    
    liquidation_manager = LiquidationManager()
    
    # Analyze BTC liquidations
    try:
        btc_liquidations = liquidation_manager.analyze_liquidation_trends(
            "BTC", interval="1h", periods=12
        )
        print(f"\nBTC Liquidation Analysis (Last 12 Hours):")
        print(f"  Total Liquidations: ${btc_liquidations['total_liquidations_usd']:,.2f}")
        print(f"  Long Liquidations: ${btc_liquidations['total_long_liquidations_usd']:,.2f}")
        print(f"  Short Liquidations: ${btc_liquidations['total_short_liquidations_usd']:,.2f}")
        print(f"  Long/Short Ratio: {btc_liquidations['long_short_ratio']:.2f}")
        print(f"  Trend: {btc_liquidations['trend'].capitalize()}")
    except Exception as e:
        print(f"Error analyzing liquidations: {e}")
    
    # Get large liquidation orders
    try:
        large_orders = liquidation_manager.get_large_liquidation_orders()
        if large_orders:
            print(f"\nRecent Large Liquidations:")
            for order in large_orders[:3]:
                print(f"  {order.get('symbol', 'N/A')}: ${order.get('liquidation_usd', 0):,.0f} "
                      f"({order.get('side', 'N/A')}) on {order.get('exchange', 'N/A')}")
    except Exception as e:
        print(f"Error getting large orders: {e}")


def demonstrate_market_indicators():
    """Demonstrate market indicators and sentiment analysis"""
    print_section("Market Indicators & Sentiment")
    
    indicators_manager = IndicatorsManager()
    
    # Get market sentiment
    try:
        sentiment = indicators_manager.get_market_sentiment_overview()
        print(f"\nMarket Sentiment Indicators:")
        
        # Fear & Greed Index
        if "fear_greed_index" in sentiment:
            fg = sentiment["fear_greed_index"]
            if "value" in fg:
                print(f"  Fear & Greed Index: {fg['value']} ({fg.get('classification', 'N/A')})")
        
        # AHR999 Index
        if "ahr999_index" in sentiment:
            ahr = sentiment["ahr999_index"]
            if "value" in ahr:
                print(f"  AHR999 Index: {ahr['value']:.2f} ({ahr.get('signal', 'N/A')})")
        
        # Coinbase Premium
        if "coinbase_premium" in sentiment:
            premium = sentiment["coinbase_premium"]
            if "value" in premium:
                print(f"  Coinbase Premium: {premium['value']:.2f}% ({premium.get('interpretation', 'N/A')})")
    except Exception as e:
        print(f"Error getting sentiment: {e}")
    
    # Get on-chain metrics
    try:
        on_chain = indicators_manager.get_on_chain_metrics()
        print(f"\nOn-Chain Metrics:")
        
        if "profitable_days_percent" in on_chain:
            print(f"  Bitcoin Profitable Days: {on_chain['profitable_days_percent']}%")
        
        if "nupl" in on_chain and isinstance(on_chain["nupl"], dict):
            nupl = on_chain["nupl"]
            print(f"  NUPL: {nupl.get('value', 'N/A')} ({nupl.get('market_phase', 'N/A')})")
    except Exception as e:
        print(f"Error getting on-chain metrics: {e}")


def demonstrate_exchange_comparison():
    """Demonstrate exchange comparison features"""
    print_section("Exchange Comparison")
    
    market_manager = MarketDataManager()
    
    try:
        btc_comparison = market_manager.compare_exchanges("BTC")
        if "volume_ranking" in btc_comparison:
            print(f"\nBTC Trading Volume by Exchange:")
            for i, exchange_data in enumerate(btc_comparison["volume_ranking"][:5], 1):
                print(f"  {i}. {exchange_data['exchange']}: ${exchange_data['volume_usd']:,.0f}")
    except Exception as e:
        print(f"Error comparing exchanges: {e}")


def main():
    """Run all demonstrations"""
    print("\n" + "="*60)
    print("CoinGlass API v4 Demonstration".center(60))
    print("="*60)
    
    # Run demonstrations
    demonstrate_basic_usage()
    demonstrate_market_analysis()
    demonstrate_liquidation_tracking()
    demonstrate_market_indicators()
    demonstrate_exchange_comparison()
    
    print(f"\n{'='*60}")
    print("Demonstration Complete".center(60))
    print("="*60 + "\n")


if __name__ == "__main__":
    main()