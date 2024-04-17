from src.bs_model import BS_Model


class Volatility_Trading(BS_Model):

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

    def straddle(self):
        """
        A straddle is a long position in both an at-the-money call and at-the-money put.
        The trader will enter into a straddle position if they believe the price will move excessively in either direction, or that the implied volatility will increase.
        However, it is important to note that the cost to enter a straddle position is expensive, as the trader needs to pay the premium for both the call and the put option.
        """
        bsm_low = BS_Model(spot=self.spot,strike=self.k_low,time= self.time, rate=self.rate,volatility= self.volatility)
        bsm_high = BS_Model(spot=self.spot, strike=self.k_high, time=self.time, rate=self.rate, volatility=self.volatility)

        return bsm_low.option_price("put") + bsm_high.option_price("put")

    def strangle(self):
        """
        A straddle is a long position in both an at-the-money call and at-the-money put. 
        The trader will enter into a straddle position if they believe the price will move excessively in either direction, or that the implied volatility will increase.
        However, it is important to note that the cost to enter a straddle position is expensive, as the trader needs to pay the premium for both the call and the put option.
        """
        bsm_low = BS_Model(spot=self.spot,strike=self.k_low,time= self.time, rate=self.rate,volatility= self.volatility)
        bsm_high = BS_Model(spot=self.spot, strike=self.k_high, time=self.time, rate=self.rate, volatility=self.volatility)

        return bsm_low.option_price("call") + bsm_high.option_price("put")
