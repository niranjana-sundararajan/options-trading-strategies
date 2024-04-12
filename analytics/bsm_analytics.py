
import pytest
from src import bs_model, credit_trading, debit_trading
import numpy as np
import matplotlib.pyplot as plt


def bs_effect_of_spot():
    k = 100
    t = 0.1
    sigma = 0.1
    r = 0.03
    s = np.arange(60,140,0.1)
    bsms = [bs_model.BS_Model(k, i, t, r, sigma) for i in s]

    calls = [bsm.option_price("call") for bsm in bsms]
    puts = [bsm.option_price("puts") for bsm in bsms]
    plt.plot(s, calls, label='Call Value')
    plt.plot(s, puts, label='Put Value')
    plt.xlabel('$S_0$')
    plt.ylabel(' Value')
    plt.legend()
    

def bs_effect_of_volatility():
    k = 100
    t = 0.1
    sigma = 0.1
    r = 0.03
    s = np.arange(60,140,0.1)
    bsms = [bs_model.BS_Model(k, i, t, r, sigma) for i in s]

    calls = [bsm.option_price("call") for bsm in bsms]
    puts = [bsm.option_price("puts") for bsm in bsms]
    plt.plot(s, calls, label='Call Value')
    plt.plot(s, puts, label='Put Value')
    plt.xlabel('$S_0$')
    plt.ylabel(' Value')
    plt.legend()

def bs_effect_of_price():
    k = 100
    t = 0.1
    sigma = 0.1
    r = 0.03
    s = np.arange(60,140,0.1)
    bsms = [bs_model.BS_Model(k, i, t, r, sigma) for i in s]

    calls = [bsm.option_price("call") for bsm in bsms]
    puts = [bsm.option_price("puts") for bsm in bsms]
    plt.plot(s, calls, label='Call Value')
    plt.plot(s, puts, label='Put Value')
    plt.xlabel('$S_0$')
    plt.ylabel(' Value')
    plt.legend()

def bs_effect_of_price():
    k = 100
    t = 0.1
    sigma = 0.1
    r = 0.03
    s = np.arange(60,140,0.1)
    bsms = [bs_model.BS_Model(k, i, t, r, sigma) for i in s]

    calls = [bsm.option_price("call") for bsm in bsms]
    puts = [bsm.option_price("puts") for bsm in bsms]
    plt.plot(s, calls, label='Call Value')
    plt.plot(s, puts, label='Put Value')
    plt.xlabel('$S_0$')
    plt.ylabel(' Value')
    plt.legend()

def bs_vega_with_time():
    stock_prices = np.arange(60,140,0.1)
    s = 100
    Ts = [1,0.75,0.5,0.25]
    k = 100
    t = 0.1
    sigma = 0.1
    r = 0.03
    bsm = bs_model.BS_Model(k, s, t, r, sigma)
    for t in Ts:
        plt.plot(bsm.vega(stock_prices, k, t, r, sigma), label=f'T = {t}')

    plt.legend()
    plt.xlabel('$S_0$')
    plt.ylabel('Vega')
    plt.title('Vega Decrease with Time')