


Reference : https://quantpreps.substack.com/p/options-trading-strategies-and-their; https://www.codearmo.com/python-tutorial/options-trading-greeks-black-scholes

# FDM Methods:

**1. Forward Difference:**

**First Order**
$$f'(x) = \frac{f(x+\Delta x) - f(x)}{\Delta x} + O(\Delta x)$$

**Second Order:**
$$ ​f''(x) = \frac{ \frac{f(x+2\Delta x) - f(x - \Delta x)}{\Delta x} - \frac{f(x+\Delta x) - f(x)} {\Delta x} }{\Delta x} = \frac{ f(x+2\Delta x) -2f(x +\Delta x)+ f(x)}{(\Delta x )^2}$$

----------------------------
**2. Backward Difference:**

**First Order**
$$f'(x) = \frac{f(x) - f(x-\Delta x) }{\Delta x} + O(\Delta x)$$

**Second Order:**
$$​​​​f''(x) = \frac{ \frac{f(x) - f(x - \Delta x)}{\Delta x} - \frac{f(x-\Delta x) - f(x -2\Delta x)} {\Delta x} }{\Delta x} = \frac{ f(x) -2f(x -\Delta x)+ f(x - 2\Delta x)}{(\Delta x )^2}$$

----------------------------
**3. Central Difference:**

**First Order**
$$f'(x) = \frac{f(x+ \Delta x) -f(x-\Delta x) }{2\Delta x} + O(\Delta x)^2$$

**Second Order:**

$$​​​​f''(x) = \frac{ \frac{f(x+\Delta x ) - f(x )}{\Delta x} - \frac{f(x) - f(x -\Delta x)} {\Delta x} }{\Delta x} = \frac{ f(x +\Delta x ) -2f(x)+ f(x -\Delta x)}{(\Delta x )^2}
$$
----------------------------
# Option Greeks
## Delta: 

Analytically, 
$$\frac{\partial C}{\partial S} = N(d_1) \hspace{0.5cm} \frac{\partial P}{\partial S} = -N(-d_1)$$

Note: The delta of an option will be between [0,1] for a call option and [-1, 0] for a put option. This should make sense in that a put option moves inversely to the price of the underlying, where a call option moves in the same direction.

FDM, 

$$\frac{\partial C}{\partial S} = \frac{BS_{Call}(S+\Delta S, K, T,r,\sigma) - BS_{Call}(S, K, T,r,\sigma)}{\Delta S}$$


## Gamma :
The formula for gamma is the same for both calls and puts. As shown below. 
Analytically:
$$\frac{\partial ^2{C}}{\partial S^2} =\frac{\partial ^2{P}}{\partial S^2} = \frac{N'(d_1)}{S\sigma\sqrt{T}}$$

FDM, 
$$\frac{\partial P}{\partial S} = \frac{BS_{Put}(S+\Delta S, K, T,r,\sigma) - 2BS_{Put}(S,K, T,r,\sigma) +BS_{Put}(S-\Delta S, K, T,r,\sigma)}{(\Delta S)^2}$$


## Vega :
Vega is the partial derivative of the option with respect to volatility.
Analytically:
$$\frac{\partial {C}}{\partial \sigma} =\frac{\partial {P}}{\partial \sigma}=S\sqrt{T} N'(d1)$$

FDM, 
$$\frac{\partial P}{\partial S} = \frac{BS_{Put}(S+\Delta S, K, T,r,\sigma) - 2BS_{Put}(S,K, T,r,\sigma) +BS_{Put}(S-\Delta S, K, T,r,\sigma)}{(\Delta S)^2}$$


## Theta :
The theta of an option is the also known as the time-decay. It measures the change of the value with respect to time. Both calls and puts will experience a decrease in value as the expiration date nears. 

Analytically:
$$\frac{\partial {C}}{\partial T} = -\frac{S \ N'\left ( d1 \right )\sigma}{2\sqrt{T}}-rKe^{-rT}N\left ( d2 \right )$$
$$\frac{\partial {P}}{\partial T} = -\frac{S \ N'\left ( d1 \right )\sigma}{2\sqrt{T}}+rKe^{-rT}N\left ( -d2 \right )$$

FDM - Here we use a backward finite difference to calculate theta on a call, 
$$\frac{\partial C}{\partial T} = \frac{BS_{Call}(S, K, T +\Delta T,r,\sigma) - BS_{Call}(S, K, T,r,\sigma)}{\Delta T}$$


## Rho :
Rho is the partial derivative of the option with respect to the risk free interest rate.  Rho will be positive for call options and negative for puts. 

Analytically:
$$\frac{\partial {C}}{\partial r} =KTe^{-rt}N\left ( d2 \right )$$
$$\frac{\partial {P}}{\partial r} =-KTe^{-rT}N\left ( -d2 \right )$$

FDM - Here we use a backward finite difference to calculate theta on a call, 
$$\frac{\partial C}{\partial r} = \frac{BS_{Call}(S, K, T ,r +\Delta r,\sigma) - BS_{Call}(S, K, T,r,\sigma)}{\Delta r}$$