#https://www.quantstart.com/articles/European-Vanilla-Call-Put-Option-Pricing-with-Python

import Statistic as sto
from math import exp, log, sqrt
from OptionPrep import OptionType, Option


class VanillaOption(Option):

    def price(self):
        if(self.Optype==OptionType.Call):
            return self.S*sto.norm_cdf(self._d_j(1))\
                -self.K*exp(-self.r*self.T) * sto.norm_cdf(self._d_j(2))
        else:
            return -self.S*sto.norm_cdf(-self._d_j(1))\
            +self.K*exp(-self.r*self.T) * sto.norm_cdf(-self._d_j(2))
            
    def _d_j(self,j):
        #Part of price calculating
        return (log(self.S/self.K) + (self.r + ((-1)**(j-1))*0.5*self.v*self.v)*self.T)\
                /(self.v*(self.T**0.5))
    
    #--- Greeks ---        
    def Delta(self):
        if(self.Optype==OptionType.Call): 
            z=1
        else: 
            z=-1
        return (z*exp(-self.r*self.T) * sto.norm_cdf(z*self._d_j(1)))
        
    def Gamma(self):
        return sto.norm_pdf(self._d_j(1))/(self.S*self.v*(self.T**0.5))
        
    