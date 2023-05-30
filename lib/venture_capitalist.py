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