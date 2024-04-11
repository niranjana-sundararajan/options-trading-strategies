import numpy as np
from scipy.stats import norm


class BS_Model:
    "Class that calculated Put and Call Prices based on BS model"

    def __init__(
        self,
        strike: float,
        spot: float,
        time: float,
        rate: float,
        volatility: float,
        dividend=None,
    ) -> None:
        self.strike = strike
        self.spot = spot
        self.time = time  # in years
        self.rate = rate  # 0 < rate < 1
        self.volatility = volatility  # 0 < volatility < 1
        self.dividend = dividend  # 0 < volatility < 1

    @property
    def params(self):
        return {
            "Spot": self.spot,
            "Strike": self.strike,
            "Time": self.time,
            "Rate": self.rate,
            "Dividend": self.dividend,
            "Volatility": self.sigma,
        }

    # -------------------------------------------------------------------------------------------------
    # Option Pricing
    # -------------------------------------------------------------------------------------------------
    def __calc_d1(self):
        return (
            np.log(self.spot / self.strike)
            + (self.rate + self.volatility**2 / 2) * self.time
        ) / (self.volatility * np.sqrt(self.time))

    def __calc_d2(self):
        return self.__calc_d1() - self.volatility * np.sqrt(self.time)

    def option_price(self, option_type: str):
        d1 = self.__calc_d1()
        d2 = self.__calc_d2()

        if option_type.lower() == "put" or option_type == "p":
            return self.strike * np.exp(-self.rate * self.time) * norm.cdf(
                -d2
            ) - self.spot * norm.cdf(-d1)
        elif option_type.lower() == "call" or option_type == "c":
            return self.spot * norm.cdf(d1) - self.strike * np.exp(
                -self.rate * self.time
            ) * norm.cdf(d2)
        else:
            raise Exception("Sorry, incorrect option type, please try again!")

    # -------------------------------------------------------------------------------------------------
    # Greeks : Analytical Calcs
    # -------------------------------------------------------------------------------------------------
    def __delta_analytical(self, option_type: str):
        N = norm.cdf
        d1 = self.__calc_d1()
        if option_type.lower() == "put" or option_type == "p":
            return N(d1)
        elif option_type.lower() == "call" or option_type == "c":
            return -N(-d1)
        else:
            raise Exception("Sorry, incorrect option type, please try again!")

    def __gamma_analytical(self):
        "Note: Gamma is the same for puts and calls"
        N_prime = norm.pdf
        d1 = self.__calc_d1()
        return N_prime(d1) / (self.spot * self.volatility * np.sqrt(self.time))

    # -------------------------------------------------------------------------------------------------
    # Greeks : FDM Calcs
    # -------------------------------------------------------------------------------------------------

    def __fdm_params(self, ds: float):
        bsm_at_s = BS_Model(
            self.strike, self.spot, self.time, self.rate, self.volatility
        )

        bsm_plus_ds = BS_Model(
            self.strike + ds, self.spot, self.time, self.rate, self.volatility
        )

        bsm_minus_ds = BS_Model(
            self.strike - ds, self.spot, self.time, self.rate, self.volatility
        )

        bsm_plus_2ds = BS_Model(
            self.strike + 2 * ds, self.spot, self.time, self.rate, self.volatility
        )

        bsm_minus_2ds = BS_Model(
            self.strike - 2 * ds, self.spot, self.time, self.rate, self.volatility
        )

        return bsm_at_s, bsm_plus_ds, bsm_minus_ds, bsm_plus_2ds, bsm_minus_2ds

    def delta(self, option_type: str, ds=1e-5, method="central"):

        bsm_at_s, bsm_plus_ds, bsm_minus_ds, _, _ = self.__fdm_params(ds)

        if method.lower() == "central" or method.lower() == "ctrl":
            delta_fdm = (
                bsm_plus_ds.option_price(option_type)
                - bsm_minus_ds.option_price(option_type)
            ) / (2 * ds)
        elif method.lower() == "forward" or method.lower() == "fwd":
            delta_fdm = (
                bsm_plus_ds.option_price(option_type)
                - bsm_at_s.option_price(option_type)
            ) / (ds)
        elif method.lower() == "backward" or method.lower() == "bwd":
            delta_fdm = (
                bsm_at_s.option_price(option_type)
                - bsm_minus_ds.option_price(option_type)
            ) / (ds)
        return delta_fdm

    def gamma(self, option_type: str, ds=1e-5, method="central"):

        bsm_at_s, bsm_plus_ds, bsm_minus_ds, bsm_plus_2ds, bsm_minus_2ds = (
            self.__fdm_params(ds)
        )

        if method.lower() == "central" or method.lower() == "ctrl":
            gamma_fdm = (
                bsm_plus_ds.option_price(option_type)
                - 2 * bsm_at_s.option_price(option_type)
                + bsm_minus_ds.option_price(option_type)
            ) / (ds**2)
        elif method.lower() == "forward" or method.lower() == "fwd":
            gamma_fdm = (
                bsm_plus_2ds.option_price(option_type)
                - 2 * bsm_plus_ds.option_price(option_type)
                + bsm_at_s.option_price(option_type)
            ) / (ds**2)
        elif method.lower() == "backward" or method.lower() == "bwd":
            gamma_fdm = (
                bsm_at_s.option_price(option_type)
                - 2 * bsm_minus_ds.option_price(option_type)
                + bsm_minus_2ds.option_price(option_type)
            ) / (ds**2)

    def vega(self, option_type: str, ds=1e-5, method="central"):
        bsm_at_s, bsm_plus_ds, bsm_minus_ds = self.__fdm_params()
        if method.lower() == "central" or method.lower() == "ctrl":
            ...
        elif method.lower() == "forward" or method.lower() == "fwd":
            ...
        elif method.lower() == "backward" or method.lower() == "bwd":
            ...

    def theta(self, option_type: str, ds=1e-5, method="central"):
        bsm_at_s, bsm_plus_ds, bsm_minus_ds = self.__fdm_params()
        if method.lower() == "central" or method.lower() == "ctrl":
            ...
        elif method.lower() == "forward" or method.lower() == "fwd":
            ...
        elif method.lower() == "backward" or method.lower() == "bwd":
            ...

    def rho(self, option_type: str, ds=1e-5, method="central"):
        bsm_at_s, bsm_plus_ds, bsm_minus_ds = self.__fdm_params()
        if method.lower() == "central" or method.lower() == "ctrl":
            ...
        elif method.lower() == "forward" or method.lower() == "fwd":
            ...
        elif method.lower() == "backward" or method.lower() == "bwd":
            ...

    # -------------------------------------------------------------------------------------------------
    # Greeks : FDM Errors
    # -------------------------------------------------------------------------------------------------
    def calc_delta_errors(self):
        return self.__delta_analytical() - self.delta()

    def calc_gamma_errors(self):
        return self.__gamma_analytical() - self.gamma()
