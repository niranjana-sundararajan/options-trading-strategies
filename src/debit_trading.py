from src.bs_model import BS_Model


class Debit_Spread_Trading(BS_Model):

    def __init__(
        self,
        spot: float,
        time: float,
        rate: float,
        volatility: float,
        k_low: float,
        k_high: float,
        strike=None,  
    ) -> None:
        super().__init__( spot, time, rate, volatility, strike=strike)
        self.k_low = k_low
        self.k_high = k_high

    def bear_put_spread(self):
        """
        Bear Put spread is where a trader buys a high strike put (higher premium) and sells a lower strike put (lower premium). The trader pays a premium upfront and is betting that the underlying price will go down.
        The premium is reduced compared to buying a put option but the potential payoff is capped.
        """
        bsm_low = BS_Model(spot=self.spot,strike=self.k_low,time= self.time, rate=self.rate,volatility= self.volatility)
        bsm_high = BS_Model(spot=self.spot, strike=self.k_high, time=self.time, rate=self.rate, volatility=self.volatility)

        return bsm_high.option_price("put") - bsm_low.option_price("put")

    def bull_call_spread(self):
        """
        Bull Call spread is where a trader buys a low strike call (higher premium) and sells a high strike call (lower premium). 
        The trader is paying a premium upfront and is betting that the underlying price will go up. The premium is reduced compared to buying a call option but potential payoff is capped.
        """
        bsm_low = BS_Model(spot=self.spot,strike=self.k_low,time= self.time, rate=self.rate,volatility= self.volatility)
        bsm_high = BS_Model(spot=self.spot, strike=self.k_high, time=self.time, rate=self.rate, volatility=self.volatility)

        return bsm_low.option_price("call") - bsm_high.option_price("call")
