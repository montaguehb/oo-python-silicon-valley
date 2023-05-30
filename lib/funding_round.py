#!/usr/bin/env python3

class FundingRound:
    all = []
    def __init__(self, startup, venture_capitalist, investment, type_):
        self._venture_capitalist = venture_capitalist
        self._startup = startup
        self.investment = investment
        self.type_ = type_
        FundingRound.all.append(self)
        
    @property
    def startup(self):
        return self._startup
    
    @startup.setter
    def startup(self, startup):
        raise AttributeError
    
    @property
    def venture_capitalist(self):
        return self._venture_capitalist
    
    @venture_capitalist.setter
    def venture_capitalist(self, venture_capitalist):
        raise AttributeError
    
    @property
    def investment(self):
        return self._investment
    
    @investment.setter
    def investment(self, investment):
        if(isinstance(investment, (float, int)) and investment > 0):
            self._investment = float(investment)
        else:
            raise ValueError
    