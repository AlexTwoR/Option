import OptionPrep as sto
from math import exp, log, sqrt
from OptionPrep import OptionType


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
        if(self.Optype==OptionType.Call): 
            z=1
        else: 
            z=-1
        return (z*exp(-self.r*self.T) * sto.norm_cdf(z*self.d_j(1)))
        
    def Gamma(self):
        return sto.norm_pdf(self.d_j(1))/(self.S*self.v*(self.T**0.5))