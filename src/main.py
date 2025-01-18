from BlackScholes import BlackScholesModel
from StockData import StockData
import streamlit as st 
import numpy as np
import matplotlib.pyplot as plt

class App:
    def __init__(self):
        return
    
    def run(self):
        # Set page layout
        st.set_page_config(page_title="Black-Scholes Dashboard", layout="wide")
        
        # Define two columns for main content and the "sidebar"
        main_col, sidebar_col = st.columns([3, 1]) 
        
        with main_col:
            # Title Styling
            st.title("📈 Black-Scholes Option Pricing Dashboard")
        
        with sidebar_col:
            # Sidebar Input Styling
            st.header("Input Parameters")
            stock_ticker = st.text_input("Stock Ticker", placeholder="e.g., AAPL")
            option_type = st.radio("Option Type", ["Call", "Put"])
            exercise_price = st.slider("Exercise Price ($)", 0.0, 500.0, 100.0, 1.0)
            time_to_maturity = st.slider("Time To Maturity (Years)", 0.1, 2.0, 1.0, 0.1)
            risk_free_rate = st.slider("Risk-Free Rate (%)", 0.0, 10.0, 5.0, 0.25)
            volatility = st.slider("Volatility (%)", 0, 100, 20, 1)
            div_yield = st.slider("Dividend Yield (%)", 0, 20, 5, 1)
        
        # Validate and Fetch Stock Data
        stock_data = StockData()
        self.validate_stock_ticker(stock_data, stock_ticker)
        S = stock_data.get_stock_price(stock_ticker)
        
        # Black-Scholes Model Calculation
        model = BlackScholesModel(
            S, exercise_price, volatility / 100, time_to_maturity, risk_free_rate / 100, div_yield=div_yield / 100, option_type=option_type
        )
        greeks = model.calculate_greeks()
        option_price = model.option_value()

        with main_col:
            # Display Stock Price
            st.subheader(f"📊 {stock_ticker.upper()} Live Price: ${S:.2f}")

            # Display Results in Cards
            st.markdown("### Option Pricing Results")
            st.info(f"**The {option_type} Option Price:** ${option_price:.2f}")
            
            # Expandable Section for Greeks
            with st.expander("View Option Greeks"):
                st.write(f"**Delta:** {greeks['Delta']:.4f}")
                st.write(f"**Gamma:** {greeks['Gamma']:.4f}")
                st.write(f"**Theta:** {greeks['Theta']:.4f}")
                st.write(f"**Vega:** {greeks['Vega']:.4f}")
                st.write(f"**Rho:** {greeks['Rho']:.4f}")
        
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