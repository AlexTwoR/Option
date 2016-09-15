#https://www.quantstart.com/articles/european-vanilla-option-pricing-with-c-via-monte-carlo-methods

import numpy as np
import Statistic as sto

from math import exp, log, sqrt
from OptionPrep import OptionType, ExerciseType, Option

class MonteCarloModel(Option):
    
    num_sims = 2000
    
    def setNumberOfSims(self,n):
        self.num_sims=n
    
    def price(self):
        
        S_adj = self.S * exp(self.T*(self.r-0.5*(self.v**2)))
        payoff_sum = 0.0
         
        for i in range(0,self.num_sims):
            gauss_bm = np.random.randn()
            S_cur = S_adj *exp(sqrt(self.T)*self.v*gauss_bm)
            payoff_sum += max(S_cur - self.K, 0.0)
    
        return ((payoff_sum/self.num_sims) * exp(-self.r*self.T))
  
  
  
