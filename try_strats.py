import numpy as np
from src import bs_model, credit_trading, debit_trading, volatility_trading
import utils


settlement_values = np.linspace(0, 200, 300)

strangle_args = {'s': 100, 
                'k_low': 90, 
                'k_high': 110, 
                't': 1, 
                'r': 0.05, 
                'sigma': 0.2}
bsm = volatility_trading.Volatility_Trading(k_low=strangle_args["k_low"],k_high=strangle_args["k_high"], spot=strangle_args["s"], time=strangle_args["t"], rate=strangle_args["r"], volatility=strangle_args["sigma"])
strangle = bsm.strangle()
# utils.plot_option_strategy(strangle, settlement_values, strangle_args)