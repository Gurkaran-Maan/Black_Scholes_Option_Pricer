import math
from scipy.stats import norm
# import mibian

class BlackScholesModel:
    
    def __init__(self, share_price, exercise_price, volatility, expiry_years, risk_free_interest, option_type = "Call", div_yield=0) -> None:
        self.S = share_price
        self.E = exercise_price
        self.vol = volatility
        self.T = expiry_years
        self.r = risk_free_interest
        self.type = option_type
        self.div_yield = div_yield
        self.option_type = option_type
        
    def option_value(self) -> int:
        d1 = (math.log(self.S/self.E) + ((self.r - self.div_yield + (self.vol**2)/2) * self.T)) / (self.vol * math.sqrt(self.T))
        d2 = d1 - (self.vol * math.sqrt(self.T))
        
        if self.option_type.lower() == "call":
            c = (self.S * math.exp(-self.div_yield*self.T) * norm.cdf(d1)) - (self.E * math.exp(-self.r * self.T) * norm.cdf(d2))
            return c
        elif self.option_type.lower() == "put":
            p = (self.E * math.exp(-self.r * self.T) * norm.cdf(-d2)) - (self.S * math.exp(-self.div_yield * self.T) * (norm.cdf(-d1)))
            return p
        else:
            return -1
        
    def calculate_greeks(self):
        d1 = (math.log(self.S/self.E) + ((self.r - self.div_yield + (self.vol**2)/2) * self.T)) / (self.vol * math.sqrt(self.T))
        d2 = d1 - (self.vol * math.sqrt(self.T))
        
        if self.option_type.lower() == "call":
            delta = math.exp(-self.div_yield * self.T) * norm.cdf(d1)
            gamma = norm.pdf(d1) * (math.exp(-self.div_yield * self.T) / (self.S * self.vol * math.sqrt(self.T)))
            theta = ((-self.S * norm.pdf(d1) * self.vol * math.exp(-self.div_yield * self.T)) / (2 * math.sqrt(self.T)) - (self.r * self.E * math.exp(-self.r * self.T) * norm.cdf(d2)) + (self.div_yield * self.S * math.exp(-self.div_yield * self.T) * norm.cdf(d1)))/365
            vega = (self.S * math.exp(-self.div_yield * self.T) * norm.pdf(d1) * math.sqrt(self.T))/100
            rho = (self.E * self.T * math.exp(-self.r * self.T) * norm.cdf(d2))/100
            return {"Delta": delta, "Gamma": gamma, "Theta": theta, "Vega": vega, "Rho": rho}
        elif self.option_type.lower() == "put":
            delta = math.exp(-self.div_yield * self.T) * (norm.cdf(d1) - 1)
            gamma = norm.pdf(d1) * (math.exp(-self.div_yield * self.T) / (self.S * self.vol * math.sqrt(self.T)))
            theta = ((-self.S * norm.pdf(d1) * self.vol * math.exp(-self.div_yield * self.T)) / (2 * math.sqrt(self.T)) + (self.r * self.E * math.exp(-self.r * self.T) * norm.cdf(-d2)) - (self.div_yield * self.S * math.exp(-self.div_yield * self.T) * norm.cdf(-d1)))/365
            vega = (self.S * math.exp(-self.div_yield * self.T) * norm.pdf(d1) * math.sqrt(self.T))/100
            rho = (-self.E * self.T * math.exp(-self.r * self.T) * norm.cdf(-d2))/100
            return {"Delta": delta, "Gamma": gamma, "Theta": theta, "Vega": vega, "Rho": rho}
        else:
            return -1