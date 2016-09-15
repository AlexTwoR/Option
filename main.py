import numpy as np
import matplotlib.pylab as plt

from OptionPrep import OptionType
from BinomialModel import BinomialModel
from VanillaOption import VanillaOption

#Define option parameters
S=100.0
K=100.0
r=0.1
v=0.3
T=365.0/365.0
Otype=OptionType.Put

#Define option     
option_bs = VanillaOption(S, K, r, v, T, Otype)
option_bin = BinomialModel(S, K, r, v, T, Otype)


#Get price and Greeks
option_bin.setNumberOfNodes(2000)
print(option_bs.price())
print(option_bin.price())

option.Delta()
option.Gamma()


#--- Option Sensitivity plot ---

#Define x aix
prices = np.arange(100)+50.0 
values = np.zeros(len(prices))

#Calc values
for p in prices:
    bufOpt=vo.VanillaOption(p, K, r, v, T, Otype)
    values[p-np.int(prices[0])]=bufOpt.Gamma()
    
plt.plot(prices, values)
