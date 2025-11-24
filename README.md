This Python project tracks the daily closing prices of multiple stocks (including NVIDIA, Apple, Tesla, Amazon, and Microsoft) over time. It calculates daily percent increases or decreases and predicts the next day's closing price using a simple average of recent changes. The project also visualizes stock price trajectories with a graph.

How It Works:

The project uses the Alpha Vantage REST API to fetch daily stock data in JSON format.

Each stock's daily data includes open, high, low, close, and volume values.

JSON Parsing:

The program parses the JSON response to extract closing prices for each day.

It stores these prices in Python lists for calculation and visualization.

Calculations:

Computes daily percent changes to track increases or decreases.

Predicts the next day's closing price using the average of recent percent changes.

Visualization:

Uses Matplotlib to plot stock price trajectories over time.

Each stock has a separate line for easy comparison.

How to Run:

Make sure Python is installed on your system.

Install required libraries:

pip install requests matplotlib
