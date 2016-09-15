import numpy as np
import Statistic as sto

from math import exp, log, sqrt
from OptionPrep import OptionType, ExerciseType, Option

class BinomialModel(Option):
    
    numberOfNodes = 10
    divR=0
    
    def setNumberOfNodes(self,n):
        self.numberOfNodes=n
    
    def price(self):
        
        z=1 if self.Optype==OptionType.Call else -1
        
        #Define array of node
        arrayNode=np.empty((self.numberOfNodes,self.numberOfNodes))
        arrayNode[:]=np.NaN
        
        dt = self.T/self.numberOfNodes

        #Calculate price up/down
        uS = exp(self.v * sqrt(dt))
        dS = exp(-self.v * sqrt(dt))
        
        print(dt)
        print(uS,dS)
        
        #Calculate probabilities
        probOfuS = (exp((self.r - self.divR) * dt) - dS) / (uS - dS)
        probOfdS = 1 - probOfuS
        
        for i in range(self.numberOfNodes-1, -1, -1):
            for j in range(0,i+1):
                if i==(self.numberOfNodes-1):
                    arrayNode[j,i]=max(0, z*((self.S * uS**(i-j) * dS**j) - self.K))

        
        return arrayNode
