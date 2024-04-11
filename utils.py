import matplotlib.pyplot as plt

import numpy as np


SETTLEMENT_VALUES = np.linspace(0, 200, 300)
STOCK_PRICES = np.arange(1, 250,1)

def plot_option_strategy(strategy_function, settlement_prices : iter, kwargs):
    
    at_expiry_kwargs = kwargs.copy()
    at_expiry_kwargs['t'] = 0
    del at_expiry_kwargs['s']
    initial_premium = strategy_function(**kwargs) 

    print('Initial premium (negative means credit)', initial_premium)

    option_payoffs = [strategy_function(settlement, **at_expiry_kwargs) - initial_premium for settlement in settlement_prices]
    
    plt.figure(figsize=(10, 8))
    plt.plot(settlement_prices, option_payoffs, label=strategy_function.__name__)
    plt.axhline(0, color='black', linestyle='--', linewidth=0.8)
    plt.xlabel('Settlement Price')
    plt.ylabel('Payoff')
    plt.title(strategy_function.__name__)
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_deltas(current_strike, stock_prices, deltas : float, option_type: str):   
    opt = option_type.capitalize()
    plt.plot(stock_prices, deltas, label = 'Delta'+ opt)
    plt.xlabel('$S_0$')
    plt.ylabel('Delta')
    plt.title('Stock Price Effect on Delta')
    plt.axvline(current_strike, color ='black', linestyle ='dashed', linewidth = 2,label = "Strike")
    plt.legend()

def plot_delta_error(stock_prices,errors, option_type: str):
    plt.plot(stock_prices, errors, label='FDM '+ option_type.capitalize + " Error")
    plt.legend()
    plt.xlabel('$S_0$')
    plt.ylabel('FDM Error')