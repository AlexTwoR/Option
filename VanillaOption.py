import OptionPrep as sto
from math import exp, log, sqrt
from statistics import OptionType


class VanillaOption:
    def __init__(self, S, K, r, v, T, Otype):
        self.S=S
        self.K=K
        self.r=r
        self.v=v
        self.T=T
        self.Optype=Otype
    
    def price(self):
        if(self.Optype==OptionType.Call):
            return self.S*sto.norm_cdf(self.d_j(1))\
            -self.K*exp(-self.r*self.T) * sto.norm_cdf(self.d_j(2))
        else:
            return -self.S*sto.norm_cdf(-self.d_j(1))\
            +self.K*exp(-self.r*self.T) * sto.norm_cdf(-self.d_j(2))
            
    def d_j(self,j):
        return (log(self.S/self.K) + (self.r + ((-1)**(j-1))*0.5*self.v*self.v)*self.T)/(self.v*(self.T**0.5))
            
    def Delta(self):
        return 0