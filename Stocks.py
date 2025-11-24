# Step 1: Import required libraries
import requests  # For making REST API calls
import matplotlib.pyplot as plt  # For plotting stock prices

# Step 2: Set up your Alpha Vantage API key
API_KEY = "WD9WKXUGGIHP1WL2"

# Step 3: Define the list of stocks to track
stocks = ["NVDA", "AAPL", "TSLA", "AMZN", "MSFT"]

# Step 4: Create a dictionary to store closing prices for each stock
stock_data = {}

# Step 5: Fetch daily stock data from Alpha Vantage
for symbol in stocks:
    # Build the API request URL for daily time series
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}"
    
    # Make the HTTP GET request
    response = requests.get(url)
    
    # Parse the JSON response
    data = response.json()
    
    # Extract the "Time Series (Daily)" data
    daily_prices = data["Time Series (Daily)"]
    
    # Sort the dates in chronological order
    sorted_dates = sorted(daily_prices.keys())
    
    # Store the closing prices as a list in stock_data dictionary
    stock_data[symbol] = [float(daily_prices[date]["4. close"]) for date in sorted_dates]

# Step 6: Define a function to calculate daily percent change
def calculate_change(prices):
    """
    Takes a list of prices and returns a list of daily percent changes.
    Positive = price increased, Negative = price decreased
    """
    changes = []
    for i in range(1, len(prices)):
        change = ((prices[i] - prices[i-1]) / prices[i-1]) * 100
        changes.append(change)
    return changes

# Step 7: Print daily percent changes for the last 5 days
print("=== Daily % changes for the last 5 days ===")
for symbol in stocks:
    changes = calculate_change(stock_data[symbol])
    print(f"{symbol}: {changes[-5:]}")  # last 5 days

# Step 8: Define a simple prediction function using average of last 5 changes
def predict_next_day(prices):
    """
    Predicts the next day's closing price using the average percent change
    from the last 5 days.
    """
    changes = calculate_change(prices)
    avg_change = sum(changes[-5:]) / len(changes[-5:])
    prediction = prices[-1] * (1 + avg_change / 100)
    return prediction

# Step 9: Print predicted next-day prices
print("\n=== Predicted next-day closing prices ===")
for symbol in stocks:
    predicted_price = predict_next_day(stock_data[symbol])
    print(f"{symbol}: ${predicted_price:.2f}")

# Step 10: Plot stock trajectories
plt.figure(figsize=(12, 6))
for symbol in stocks:
    plt.plot(stock_data[symbol], label=symbol)

plt.title("Stock Closing Prices Over Time")
plt.xlabel("Days")
plt.ylabel("Price ($)")
plt.legend()
plt.grid(True)
plt.show()
