from BlackScholes import BlackScholesModel
from StockData import StockData

## convert to OOP

class App:
    def __init__(self):
        return

    def run(self):
        option_type = input("Option Type: ")
        
        self.validate_option_type(option_type)
        
        ticker = input("Enter Stock Ticker Symbol: ")
        
        stock_data = StockData()
        
        self.validate_stock_ticker(stock_data, ticker)
        
        S = stock_data.get_stock_price(ticker)
        
        #float(input("Enter Share Price: "))
        E = input("Enter Exercise Price: ")
        T = input("Enter time to expiry in years: ")
        V = input("Enter Volatility: ")
        r = input("Enter the risk free interest rate: ")
        div_yield = input("Enter the dividend yield: ")
        
        E, T, V, r, div_yield = self.validate_numerical_input([E, T, V, r, div_yield])
        
        model = BlackScholesModel(S, E, V, T, r, div_yield=div_yield, option_type=option_type)
        print(model.option_value())
        
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