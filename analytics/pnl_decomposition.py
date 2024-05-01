import sys,os
src_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, "c:/Quant-Fin/strategies/options-trading-strategies/") 

from  src import bs_model
import numpy as np
import matplotlib.pyplot as plt



#parameters
S0 = 100 # stock price
K = 95 # strike price
r = 0.03 # risk-free interest rate
q = 0.0 # dividend
T0 = 0.25 # time to maturity
sigma0 = 0.4 # implied volatility BS
op_type = "put"
dt = 1 / 252 # 1 business day

# Market changes between t and t + dt 
dS = -S0 * .6 * dt**.5 # realised vol = .6
dsigma = .1
T1 = T0 - dt
S1 = S0 + dS
sigma1 = sigma0 + dsigma

# We calculate the P&L between t and t + δt
bsm0 = bs_model.BS_Model(spot=S0, time=T0, rate=r, volatility=sigma0,strike=K )
bsm1 = bs_model.BS_Model(spot=S1, time=T1, rate=r, volatility=sigma1,strike=K )
p0 = bsm0.option_price(option_type= op_type)
p1 = bsm1.option_price(option_type= op_type)

# Assuming some level of delta hedge
delta0 = bsm0.delta_analytical(option_type=op_type)
delta01 = bsm0.delta(option_type=op_type)
isDeltaHedged = 1 # 1 if is delta-hedged, 0 otherwise
dPnL = p1 - p0 - delta0 * dS * isDeltaHedged # assuming some level of delta hedge
print("P&L: " + str(dPnL))
print("delta0: " , str(delta0) + " " + str(delta01))



# We decompose the P&L between the contribution of the different Greeks and we plot it with a barchart
# Initial greeks
theta0 = bsm0.theta(option_type=op_type)
vega0 = bsm0.vega(option_type=op_type)
gamma0 = bsm0.gamma(option_type=op_type)
volga0 = bsm0.volga(option_type=op_type)
vanna0 = bsm0.vanna(option_type=op_type)
print("Theta :{float}, Vega : {float} , Gamma : {float} , Volga : {float}, Vanna : {float}", theta0, vega0, gamma0, volga0, vanna0)

# P&L attribution
delta_PnL = delta0 * dS * (1 - isDeltaHedged)
theta_PnL = theta0 * dt
vega_PnL = vega0 * dsigma
gamma_PnL = 1 / 2 * gamma0 * dS**2
volga_PnL = 1 / 2 * volga0 * dsigma**2
vanna_PnL = vanna0 * dS * dsigma
unexplained = dPnL - sum([delta_PnL, theta_PnL, vega_PnL, gamma_PnL, volga_PnL, vanna_PnL])

y = [delta_PnL, theta_PnL, vega_PnL, gamma_PnL, volga_PnL, vanna_PnL, unexplained]
x = ["delta", "theta", "vega", "gamma", "volga", "vanna","unexplained"]

fig = plt.figure(figsize=(15, 5))
plt.bar(x, y)
plt.title("P&L Decomposition")
plt.show()