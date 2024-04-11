import pytest
from src import bs_model, credit_trading, debit_trading
import numpy as np

settlement_values = np.linspace(0, 200, 300)

def test_bs_option_pricing():
    s = 100
    k = 100
    t = 1
    sigma = 0.1
    r = 0.03
    bsm = bs_model.BS_Model(k, s, t, r, sigma)
    assert round(bsm.option_price("put"),4) == 2.6264
    assert round(bsm.option_price("call"),4) == 5.5819


def test_bs_greeks():
    ...