from math import exp, log, sqrt
import statistics as sto
from enum import Enum

OptionType = Enum('OptionType', 'Call Put')

#from statistics import norm_pdf, norm_cfd


#----- Pricing -----

def d_j(j, S, K, r, v, T):
    """d_j = \frac{log(\frac{S}{K})+(r+(-1)^{j-1} \frac{1}{2}v^2)T}{v sqrt(T)}"""
    return (log(S/K) + (r + ((-1)**(j-1))*0.5*v*v)*T)/(v*(T**0.5))
    

def vanilla_call_price(S, K, r, v, T):
    """Price of a European call option struck at K, with spot S, 
    constant rate r, constant vol v (over the life of the option) and time to maturity T"""
    return S*sto.norm_cdf(d_j(1, S, K, r, v, T))-K*exp(-r*T) * sto.norm_cdf(d_j(2, S, K, r, v, T))
    
def vanilla_put_price(S, K, r, v, T):
    """Price of a European put option struck at K, with spot S, 
    constant rate r, constant vol v (over the life of the option) and time to maturity T"""
    return -S*sto.norm_cdf(-d_j(1, S, K, r, v, T))+K*exp(-r*T) * sto.norm_cdf(-d_j(2, S, K, r, v, T))
    
def vanilla_option_price(S, K, r, v, T, Otype):
    if(Otype==OptionType.Call):
        return S*sto.norm_cdf(d_j(1, S, K, r, v, T))-K*exp(-r*T) \
                                * sto.norm_cdf(d_j(2, S, K, r, v, T))
    else:
        return -S*sto.norm_cdf(-d_j(1, S, K, r, v, T))+K*exp(-r*T) \
                                * sto.norm_cdf(-d_j(2, S, K, r, v, T))
    
    
#----- Greeks -----




S=100.0
K=100.0
r=0.1
v=0.3
T=365.0/365.0
Otype=OptionType.Put


vanilla_option_price(S, K, r, v, T, Otype)

