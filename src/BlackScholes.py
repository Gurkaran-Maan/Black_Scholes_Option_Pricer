import math
from scipy.stats import norm

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
        
        if self.option_type == "Call":
            c = (self.S * math.exp(-self.div_yield*self.T) * norm.cdf(d1)) - (self.E * math.exp(-self.r * self.T) * norm.cdf(d2))
            return c
        else:
            p = (self.E * math.exp(-self.r * self.T) * norm.cdf(-d2)) - (self.S * math.exp(-self.div_yield * self.T) * (norm.cdf(-d1)))
            return p