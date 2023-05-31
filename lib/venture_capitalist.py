#!/usr/bin/env python3

from funding_round import FundingRound

class VentureCapitalist:
    all = []
    def __init__(self, name, total_worth):
        self.name = name
        self.total_worth = total_worth
        VentureCapitalist.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if(isinstance(name, str)):
            self._name = name
        else:
            raise AttributeError
    
    @property
    def total_worth(self):
        return self._total_worth
    
    @total_worth.setter
    def total_worth(self, total_worth):
        if isinstance(total_worth, (int, float)):
            self._total_worth = float(total_worth)
        else:
            raise ValueError
    
    @classmethod
    def tres_commas_club(cls):
        return [investor for investor in cls.all if investor.total_worth >= 1000000000]
    
    def offer_contract(self, startup, type_, investment):
        FundingRound(startup=startup, venture_capitalist=self, type_=type_, investment=investment)
        
    def funding_rounds(self):
        return [fr for fr in FundingRound.all if fr.venture_capitalist == self]
    
    def portfolio(self):
        startups = []
        for fr in self.funding_rounds():
            if(fr.startup not in startups and fr.venture_capitalist == self):
                startups.append(fr.startup)
        return startups
    
    def biggest_investment(self):
        largest = None
        for fr in self.funding_rounds():
            if largest is None or fr.investment > largest.investment:
                largest = fr
        return largest
    
    def invested(self, domain):
        return sum((fr.investment for fr in self.funding_rounds() if fr.startup.domain == domain))