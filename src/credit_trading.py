
from src.bs_model import BS_Model

class Credit_Spread_Trading(BS_Model):

    def __init__(self, k_low: float,k_high: float, spot: float, time: float, rate: float, volatility: float) -> None:
        super().__init__(spot, time, rate, volatility)
        self.k_low = k_low
        self.k_high = k_high

    def bull_put_spread(self):
        """Bull Put spread is where a trader sells a high strike put (higher premium) and buys a lower strike put (lower premium). 
        The trader receives a premium upfront and is hoping that the underlying price stays the same or doesn’t go down."""
        bsm_low = BS_Model(self.spot, self.k_low, self.t, self.rate, self.sigma)
        bsm_high = BS_Model(self.spot, self.k_high, self.t, self.rate, self.sigma)
        
        return bsm_low.option_price("put") - bsm_high.option_price("put")
    
    def bear_call_spread(self):
        """Bear Call spread is where a trader sells a low strike call (higher premium) and buys a high strike call (lower premium). 
        The trader receives a premium upfront and hoping that the underlying price stays the same or doesn’t go up."""
        bsm_low = BS_Model(self.spot, self.k_low, self.t, self.rate, self.sigma)
        bsm_high = BS_Model(self.spot, self.k_high, self.t, self.rate, self.sigma)
        
        return bsm_high.option_price("call") - bsm_low.option_price("call")