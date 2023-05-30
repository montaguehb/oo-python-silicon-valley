#!/usr/bin/env python3

from funding_round import FundingRound

class VentureCapitalist:
    all = []
    def __init__(self, name):
        self.name = name
        VentureCapitalist.all.append(self)
