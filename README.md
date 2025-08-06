# CoinGlass API v4 Integration

This repository contains a Python implementation for interacting with the CoinGlass API v4, a comprehensive platform for cryptocurrency derivatives data, including futures, options, liquidations, market indicators, and on-chain metrics.

**Repository**: https://github.com/SnakeO/Coinglass-APIv4

## Features

### Core Managers
- **TopPairsManager**: Retrieve the top trading pairs across exchanges
- **FundingRateManager**: Get real-time and historical funding rates
- **LongShortRatioManager**: Access long/short ratio data for trading pairs
- **LiquidationManager**: Comprehensive liquidation data and analysis
- **IndicatorsManager**: Market sentiment indicators (Fear & Greed, AHR999, etc.)
- **MarketDataManager**: Market overview, coin analysis, and exchange comparisons

### Services Available
- **Price Data**: Historical price information
- **Liquidation Data**: Real-time and historical liquidation tracking
- **Open Interest**: Open interest by exchange and historical data
- **Market Data**: Coins markets, pairs markets, price changes
- **Indicators**: 30+ on-chain and market indicators
- **Options**: Options flow, volume, and statistics
- **Spot Market**: Spot market data and statistics
- **ETF**: Bitcoin ETF holdings and flow data
- **Exchange Data**: Exchange rankings and statistics
- **Order Book**: Order book depth and large order tracking

## Installation

To get started, clone this repository and install dependencies. Here you can use `poetry`.

- `poetry shell`
- `poetry install`


## API Key
All endpoints require an API key for authentication. Make sure to sign up for a CoinGlass account and check the API documentation for specific authentication instructions. You will need to setup your API key
- run `cp .env.example .env`
- change `BASE_API_KEY` value inside `.env`

## Usage

### Basic Example

```python
from managers.top_pairs import TopPairsManager
from managers.funding_rate import FundingRateManager
from managers.liquidation_manager import LiquidationManager

# Get the top trading pairs
top_pairs_manager = TopPairsManager()
top_pairs = top_pairs_manager.get_top_pairs(top_n=10)

# Get funding rates for the top pairs
funding_rate_manager = FundingRateManager()
funding_rates = funding_rate_manager.get_funding_rate(top_pairs)

print(funding_rates)
```

### Market Analysis Example

```python
from managers.market_data_manager import MarketDataManager
from managers.indicators_manager import IndicatorsManager

# Initialize managers
market_manager = MarketDataManager()
indicators_manager = IndicatorsManager()

# Get market overview for top 10 coins
market_overview = market_manager.get_market_overview(top_n=10)
print(f"Total Market Cap: ${market_overview['total_market_metrics']['total_market_cap_usd']:,.2f}")

# Get current market sentiment
sentiment = indicators_manager.get_market_sentiment_overview()
print(f"Fear & Greed Index: {sentiment['fear_greed_index']['value']} ({sentiment['fear_greed_index']['classification']})")

# Analyze specific coin
btc_analysis = market_manager.get_coin_analysis("BTC")
print(f"BTC 24h Price Change: {btc_analysis['price_changes']['price_change_percent_24h']}%")
```

### Liquidation Tracking Example

```python
from managers.liquidation_manager import LiquidationManager

liquidation_manager = LiquidationManager()

# Get liquidation trends for Bitcoin
btc_trends = liquidation_manager.analyze_liquidation_trends("BTC", interval="1h", periods=24)
print(f"Total BTC Liquidations (24h): ${btc_trends['total_liquidations_usd']:,.2f}")
print(f"Long/Short Ratio: {btc_trends['long_short_ratio']:.2f}")
print(f"Trend: {btc_trends['trend']}")

# Get large liquidation orders
large_orders = liquidation_manager.get_large_liquidation_orders()
for order in large_orders[:5]:
    print(f"{order['symbol']}: ${order['liquidation_usd']:,.2f} ({order['side']}) on {order['exchange']}")
```

### On-Chain Metrics Example

```python
from managers.indicators_manager import IndicatorsManager

indicators = IndicatorsManager()

# Get on-chain metrics
on_chain = indicators.get_on_chain_metrics()
print(f"Bitcoin Profitable Days: {on_chain['profitable_days_percent']}%")
print(f"NUPL Market Phase: {on_chain['nupl']['market_phase']}")

# Get valuation metrics
valuation = indicators.get_valuation_metrics()
print(f"Puell Multiple: {valuation['puell_multiple']}")
print(f"Stock-to-Flow Model: {valuation['stock_to_flow']}")
```

### Exchange Comparison Example

```python
from managers.market_data_manager import MarketDataManager

market_manager = MarketDataManager()

# Compare Bitcoin metrics across exchanges
btc_comparison = market_manager.compare_exchanges("BTC")
print("\nBTC Volume by Exchange:")
for exchange_data in btc_comparison['volume_ranking'][:5]:
    print(f"{exchange_data['exchange']}: ${exchange_data['volume_usd']:,.2f}")

# Get top performing pairs on Binance
binance_pairs = market_manager.get_pairs_performance("Binance", top_n=10)
for pair in binance_pairs[:5]:
    print(f"{pair['symbol']}: Volume ${pair['volume_usd']:,.2f}, Funding Rate {pair['funding_rate']:.4f}%")
```

## API Endpoints

The v4 API provides the following main endpoint categories:

### Futures Endpoints
- `/futures/funding-rate/*` - Funding rate data and history
- `/futures/long-short-ratio/*` - Long/short positioning data
- `/futures/liquidation/*` - Liquidation data and heatmaps
- `/futures/open-interest/*` - Open interest by exchange and history
- `/futures/orderbook/*` - Order book depth and large orders
- `/futures/price/*` - Price history data

### Market Data Endpoints
- `/indicator/coins-markets` - Cryptocurrency market data
- `/indicator/pairs-markets` - Trading pairs market data
- `/indicator/coins-price-change` - Price change statistics
- `/indicator/exchange-rank` - Exchange rankings

### Bitcoin Indicators
- `/indicator/bitcoin/fear-greed-index` - Fear & Greed Index
- `/indicator/bitcoin/rainbow-chart` - Rainbow Chart data
- `/indicator/bitcoin/ahr999` - AHR999 Index
- `/indicator/bitcoin/puell-multiple` - Puell Multiple
- `/indicator/bitcoin/stock-to-flow` - Stock-to-Flow model
- `/indicator/bitcoin/nupl` - Net Unrealized Profit/Loss
- And 20+ more indicators

### Options Data
- `/indicator/options/flow` - Options flow data
- `/indicator/options/volume` - Options volume
- `/indicator/options/statistics` - Options statistics

### Spot Market
- `/indicator/spot-statistics` - Spot market statistics
- `/indicator/stablecoin-statistics` - Stablecoin metrics

### ETF Data
- `/indicator/etf/holdings` - ETF holdings data
- `/indicator/etf/flow` - ETF flow data

## Error Handling

All API responses follow a standard format:

```python
{
    "code": "0",  # "0" for success, error code otherwise
    "msg": "success",  # Error message if applicable
    "data": {...}  # Response data
}
```

Example error handling:

```python
try:
    data = manager.get_some_data()
    if data.get("code") != "0":
        print(f"API Error: {data.get('msg')}")
    else:
        # Process successful response
        process_data(data.get("data"))
except Exception as e:
    print(f"Request failed: {str(e)}")
```

## Rate Limits

Please refer to the official CoinGlass API documentation for current rate limit information. The client includes automatic retry logic for rate limit errors.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer

This is an unofficial Python client for the CoinGlass API. Please refer to the official CoinGlass documentation for the most up-to-date API information.
