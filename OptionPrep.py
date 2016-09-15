from enum import Enum

#Define the types of option
OptionType = Enum('OptionType', 'Call Put')
ExerciseType = Enum('ExerciseType', 'European American')


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
        

