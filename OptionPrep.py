from enum import Enum

#Define the types of option
OptionType = Enum('OptionType', 'Call Put')
ExerciseType = Enum('OptionType', 'European American')


class Option:
    def __init__(self, S, K, r, v, T, Otype):
        self.S=S
        self.K=K
        self.r=r
        self.v=v
        self.T=T
        self.Optype=Otype
    
    def __repr__(self):
        return "Spot: {0}\nStrike: {1}\nRate: {2}\nVoltility: {3}\nTime: {4}"\
        .format(self.S,self.K,self.r,self.v,self.T)
        


"""
#Probability density
def norm_cdf(x):
    #An approximation to the cumulative distribution function for the standard normal distribution:
    
    k = 1.0/(1.0+0.2316419*x)
    k_sum = k*(0.319381530 + k*(-0.356563782 + k*(1.781477937 + k*(-1.821255978 + 1.330274429*k))))

    if x >= 0.0:
        return (1.0 - (1.0/((2*pi)**0.5))*exp(-0.5*x*x) * k_sum)
    else:
        return 1.0 - norm_cdf(-x)


def norm_pdf(x):
    #Standard normal probability density function
    return (1.0/((2*pi)**0.5))*exp(-0.5*x*x)
"""