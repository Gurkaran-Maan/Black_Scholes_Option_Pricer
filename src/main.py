from BlackScholes import BlackScholesModel
from StockData import StockData
import streamlit as st 
import numpy as np
import matplotlib.pyplot as plt

class App:
    def __init__(self):
        return

    def run(self):
        st.title("Black-Scholes Option Pricing Dashboard")
        
        st.sidebar.header("Input Parameters")
        stock_ticker = st.sidebar.text_input("Stock Ticker", placeholder="AAPL")
        option_type = st.sidebar.radio("Option Type", ["Call", "Put"])
        exercise_price = st.sidebar.slider("Exercise Price", 0.0, 500.0, 100.0, 1.0)
        time_to_maturity = st.sidebar.slider("Time To Maturity(Years)", 0.1, 2.0, 1.0, 0.1)
        risk_free_rate = st.sidebar.slider("Risk Free Rate(%)", 0, 10, 5, 1)
        volatility = st.sidebar.slider("Volatility(%)", 0, 100, 20, 1)
        div_yield = st.sidebar.slider("Dividend Yield(%)", 0, 20, 5, 1)
        
        stock_data = StockData()
        
        self.validate_stock_ticker(stock_data, stock_ticker)
        
        S = stock_data.get_stock_price(stock_ticker)
        
        st.write("You have selected the following parameters:")
        st.write(f"Stock Ticker: {stock_ticker}")
        st.write(f"Stock Price: {S}")
        st.write(f"Option Type: {option_type}")
        st.write(f"Exercise Price: {exercise_price}")
        st.write(f"Time To Maturity: {time_to_maturity}")
        st.write(f"Risk Free Rate: {risk_free_rate}")
        st.write(f"Volatility: {volatility}")
        st.write(f"Dividend Yield: {div_yield}")
        
        model = BlackScholesModel(S, exercise_price, volatility/100, time_to_maturity, risk_free_rate/100, div_yield=div_yield/100, option_type=option_type)
        st.write(f"The {option_type} Option Price is: ${model.option_value()}")
        
        # st.pyplot(plt)
        
    def validate_numerical_input(self, inputs):
        outputs = []
        try:
            for input in inputs:
                outputs.append(float(input))
            return outputs
        except ValueError:
            print("Invalid input. Please ensure all fields are numerical.")
            exit()
            
    def validate_option_type(self, option_type):
        if option_type.lower() not in ["call", "put"]:
            print("Invalid option type. Please enter either 'call' or 'put'")
            exit()
            
    def validate_stock_ticker(self, stock_data, ticker):
        if not stock_data.is_valid_ticker(ticker):
            print("Invalid stock ticker. Please enter a valid stock ticker.")
            exit()

if __name__ == "__main__":
    app = App()
    app.run()