import yfinance as yf
import json

# List of tickers to represent
tickers = ["AAPL", "MSFT", "GOOGL", "AMZN", "META", "TSLA", "NVDA", "BRK-B", "JNJ", "V"]

# Loop through each ticker and fetch historical data
for ticker in tickers:
    try:
        stock = yf.Ticker(ticker)
        data = stock.history(period="10y")
        data.reset_index(inplace=True)

        # Create a list of dictionaries with necessary data
        stock_data = []
        for _, row in data.iterrows():
            stock_data.append({
                "date": row['Date'].strftime('%Y-%m-%d'),
                "market_valuation": row['Close'] * row['Volume']  # Using close price multiplied by volume as a proxy for valuation
            })

        # Save the data to a JSON file
        with open(f"{ticker.lower().replace('.', '_')}_data.json", "w") as f:
            json.dump(stock_data, f)
    except Exception as e:
        print(f"Failed to fetch data for {ticker}: {e}")
