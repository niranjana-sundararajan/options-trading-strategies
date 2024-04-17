import pytest
from src import bs_model, credit_trading, debit_trading, volatility_trading
import utils
import numpy as np

settlement_values = np.linspace(0, 200, 300)


def test_bs_model():
    s = 100
    k = 90
    t =1 
    sigma = 0.4
    r = 0.03
    bsm = bs_model.BS_Model(k, s, t, r, sigma)
    assert bsm.option_price("call") != 0

# --------------------------------------------------------------------------------------------------------------------------------
# Volatility Trading
# --------------------------------------------------------------------------------------------------------------------------------
def test_strangle():
    strangle_args = {'s': 100, 
                    'k_low': 90, 
                    'k_high': 110, 
                    't': 1, 
                    'r': 0.05, 
                    'sigma': 0.2}
    bsm = volatility_trading.Volatility_Trading(k_low=strangle_args["k_low"],k_high=strangle_args["k_high"], spot=strangle_args["s"], time=strangle_args["t"], rate=strangle_args["r"], volatility=strangle_args["sigma"])
    strangle = bsm.strangle()
    assert strangle != 0

def test_straddle():
    straddle_args = {'s': 100, 
                    'k_low': 90, 
                    'k_high': 110, 
                    't': 1, 
                    'r': 0.05, 
                    'sigma': 0.2}
    bsm = volatility_trading.Volatility_Trading(k_low=straddle_args["k_low"],k_high=straddle_args["k_high"], spot=straddle_args["s"], time=straddle_args["t"], rate=straddle_args["r"], volatility=straddle_args["sigma"])
    straddle = bsm.straddle()
    assert straddle != 0
# --------------------------------------------------------------------------------------------------------------------------------
# Debit Spread Trading
# --------------------------------------------------------------------------------------------------------------------------------
def test_bull_call_spread():
    bull_call_spread_args = {'s': 90, 
                         'k_low': 100,
                         'k_high': 110, 
                         't': 1, 
                         'r': 0.05, 
                         'sigma': 0.2}
    bsm = debit_trading.Debit_Spread_Trading(k_low=bull_call_spread_args["k_low"],k_high=bull_call_spread_args["k_high"], spot=bull_call_spread_args["s"], time=bull_call_spread_args["t"], rate=bull_call_spread_args["r"], volatility=bull_call_spread_args["sigma"])
    bull_call_spread = bsm.bull_call_spread()
    assert bull_call_spread != 0

def test_bear_put_spread():
    bear_put_spread_args = {'s': 110, 
                        'k_low': 90, 
                        'k_high': 100, 
                        't': 1, 
                        'r': 0.05, 
                        'sigma': 0.2}
    bsm = debit_trading.Debit_Spread_Trading(k_low=bear_put_spread_args["k_low"],k_high=bear_put_spread_args["k_high"], spot=bear_put_spread_args["s"], time=bear_put_spread_args["t"], rate=bear_put_spread_args["r"], volatility=bear_put_spread_args["sigma"])
    bear_put_spread = bsm.bear_put_spread()
    assert bear_put_spread != 0

# --------------------------------------------------------------------------------------------------------------------------------
# Credit Spread Trading
# --------------------------------------------------------------------------------------------------------------------------------

def test_bear_call_spread():
    bear_call_spread_args = {'s': 70, 
                         'k_low': 80, 
                         'k_high': 100, 
                         't': 1,
                         'r': 0.05, 
                         'sigma': 0.2}

    bsm = credit_trading.Credit_Spread_Trading(k_low=bear_call_spread_args["k_low"],k_high=bear_call_spread_args["k_high"], spot=bear_call_spread_args["s"], time=bear_call_spread_args["t"], rate=bear_call_spread_args["r"], volatility=bear_call_spread_args["sigma"])
    bear_call_spread = bsm.bear_call_spread()
    assert bear_call_spread != 0

def test_bull_put_spread():
    bull_put_spread_args = {'s': 110, 
                        'k_low': 80, 
                        'k_high': 100, 
                        't': 1, 
                        'r': 0.05, 
                        'sigma': 0.2} 

    bsm = credit_trading.Credit_Spread_Trading(k_low=bull_put_spread_args["k_low"],k_high=bull_put_spread_args["k_high"], spot=bull_put_spread_args["s"], time=bull_put_spread_args["t"], rate=bull_put_spread_args["r"], volatility=bull_put_spread_args["sigma"])
    bull_put_spread = bsm.bull_put_spread()
    assert bull_put_spread != 0