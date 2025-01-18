import datetime as dt
import pandas as pd
import yfinance as yf


class StockData():
    
    def __init__(self):
        return
    
    def get_stock_price(self, ticker: str) -> float:
        
        start = dt.datetime(2024, 10, 24)
        end = dt.datetime.now()
        
        ticker = yf.Ticker(ticker)
        
        return ticker.history(period="1d", interval="1m").iloc[-1]['Close']
    
    def is_valid_ticker(self, ticker):
        try:
            stock = yf.Ticker(ticker)
            # Check if the ticker has historical market data
            if stock.history(period="1d").empty:
                return False  # No data means the ticker is likely invalid
            return True
        except Exception as e:
            return False  # Any exception implies the ticker is invalid
