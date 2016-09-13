import VanillaOption as vo
from OptionPrep import OptionType

S=100.0
K=100.0
r=0.1
v=0.3
T=365.0/365.0
Otype=OptionType.Call
       
option=vo.VanillaOption(S, K, r, v, T, Otype)

option.price()



