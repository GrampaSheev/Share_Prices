import yfinance as yf

AMD = yf.Ticker("AMD")

print(AMD.recommendations)