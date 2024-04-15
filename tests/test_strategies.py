import pytest
from src import bs_model, credit_trading, debit_trading
import numpy as np

settlement_values = np.linspace(0, 200, 300)


def test_bs_model():
    s = 100
    k = 100
    t = 0.1
    sigma = 0.1
    r = 0.03
    bsm = bs_model.BS_Model(k, s, t, r, sigma)
    assert bsm.option_price("put") != 0
