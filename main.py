import numpy as np
import matplotlib.pylab as plt

from OptionPrep import OptionType
from BinomialModel import BinomialModel
from VanillaOption import VanillaOption
from MonteCarloModel import MonteCarloModel

#Define option parameters
S=100.0  #Option price
K=100.0  #Strike price
r=0.1  #Risk-free rate
v=0.3  #Volatility of the underlying
T=365.0/365.0  #Time until expiry 
Otype=OptionType.Call

#Define option     
option_bs = VanillaOption(S, K, r, v, T, Otype)
option_bin = BinomialModel(S, K, r, v, T, Otype)
option_mc = MonteCarloModel(S, K, r, v, T, Otype)

#Get price and Greeks
print(option_bs.price())
print(option_bin.price())
print(option_mc.price())


#--- Option Sensitivity plot ---

#Define x aix
prices = np.arange(100)+50.0 
values = np.zeros(len(prices))

#Calc values
for p in prices:
    bufOpt=VanillaOption(p, K, r, v, T, Otype)
    values[p-np.int(prices[0])]=bufOpt.Gamma()
    
plt.plot(prices, values)