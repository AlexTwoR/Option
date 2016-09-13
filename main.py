import VanillaOption as vo
import numpy as np
import matplotlib.pylab as plt
from OptionPrep import OptionType

S=100.0
K=100.0
r=0.05
v=0.1
T=365.0/365.0
Otype=OptionType.Call
       
option=vo.VanillaOption(S, K, r, v, T, Otype)
option.price()
option.Delta()
option.Gamma()

prices = np.arange(100)+50.0 
values=np.zeros(len(prices))


for p in prices:
    bufOpt=vo.VanillaOption(p, K, r, v, T, Otype)
    values[p-np.int(prices[0])]=bufOpt.Gamma()
    
plt.plot(prices, values)


OptionType.Call==Otype