


Reference : https://quantpreps.substack.com/p/options-trading-strategies-and-their

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

$$\frac{\partial C}{\partial S} = \frac{BS_{Call}(S+\Delta S, K, T,r,\sigma) - BS_{Call}(S, K, T,r,\sigma)}{\Delta S}$$


## Gamma :

Analytically:
$$\frac{\partial ^2{C}}{\partial S^2} =\frac{\partial ^2{P}}{\partial S^2} = \frac{N'(d_1)}{S\sigma\sqrt{T}}$$


$$\frac{\partial P}{\partial S} = \frac{BS_{Put}(S+\Delta S, K, T,r,\sigma) - 2BS_{Put}(S,K, T,r,\sigma) +BS_{Put}(S-\Delta S, K, T,r,\sigma)}{(\Delta S)^2}$$
