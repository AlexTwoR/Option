import VanillaOption as vo
import numpy as np
import matplotlib.pylab as plt
from OptionPrep import OptionType
from AmericanOption import AmericanOption

#Define option parameters
S=100.0
K=100.0
r=0.1
v=0.3
T=365.0/365.0
Otype=OptionType.Call

#Define option     
#option=vo.VanillaOption(S, K, r, v, T, Otype)
option=AmericanOption(S, K, r, v, T, Otype)

#Get price and Greeks

#--- Testing ---
option.setNumberOfNodes(20)
rooo=option.price()

plt.plot(rooo[:,19])
#------

option.price()
option.Delta()
option.Gamma()

option


#--- Option plot ---

#Define x aix
prices = np.arange(100)+50.0 
values=np.zeros(len(prices))

#Calc values
for p in prices:
    bufOpt=vo.VanillaOption(p, K, r, v, T, Otype)
    values[p-np.int(prices[0])]=bufOpt.Gamma()
    
plt.plot(prices, values)
