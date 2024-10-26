import datetime as dt
import pandas as pd
import yfinance as yf


class StockData():
    
    def __init__(self):
        return
    
    def get_stock_price(self, ticker: str) -> float:
        
        start = dt.datetime(2024, 10, 24)
        end = dt.datetime.now()
        
        # data = web.DataReader(ticker, 'yahoo', start, end)
        
        ticker = yf.Ticker(ticker)
        
        return ticker.history(period="1d", interval="1m").iloc[-1]['Close']
