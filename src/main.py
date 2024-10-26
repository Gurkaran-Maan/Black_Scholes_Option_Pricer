from BlackScholes import BlackScholesModel
from StockData import StockData

## convert to OOP

if __name__ == "__main__":
    option_type = input("Option Type: ")
    
    ticker = input("Enter Stock Ticker Symbol: ")
    
    stock_data = StockData()
    S = stock_data.get_stock_price(ticker)
    
    
    #float(input("Enter Share Price: "))
    E = float(input("Enter Exercise Price: "))
    T = float(input("Enter time to expiry in years: "))
    V = float(input("Enter Volatility: "))
    r = float(input("Enter the risk free interest rate: "))
    
    div_yield = float(input("Enter the dividend yield: "))
    
    model = BlackScholesModel(S, E, V, T, r, div_yield=div_yield, option_type=option_type)
    print(model.option_value())