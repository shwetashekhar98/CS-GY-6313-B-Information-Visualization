import yfinance as yf
import json

# List of tickers
tickers = ["AAPL", "MSFT", "GOOGL", "AMZN", "META", "TSLA", "NVDA", "BRK-B", "JNJ", "V"]

# Fetch data for each ticker
for ticker in tickers:
    stock = yf.Ticker(ticker)
    data = stock.history(period="1y")
    data.reset_index(inplace=True)
    
    # Prepare the data for JSON export
    stock_data = [
        {"date": row['Date'].strftime('%Y-%m-%d'), "value": row['Close']} 
        for _, row in data.iterrows()
    ]
    
    # Save data to JSON file
    filename = f"{ticker.lower().replace('-', '_')}_data.json"
    with open(filename, "w") as f:
        json.dump(stock_data, f)

print("Data fetching and saving completed.")
