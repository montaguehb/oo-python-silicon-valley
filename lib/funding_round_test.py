import unittest
from funding_round import FundingRound
from venture_capitalist import VentureCapitalist
from startup import Startup

class Founding_Round_Test(unittest.TestCase):
    def test_has_startup(self):
        startup = Startup(name="svb", founder="Greg Becker", domain="svb.com")
        funding_round = FundingRound(startup=startup)
        self.assertEqual(startup, funding_round.startup)
        Startup.all = []
        VentureCapitalist.all = []
        FundingRound.all = []
    def test_startup_is_immutable(self):
        startup = Startup(name="svb", founder="Greg Becker", domain="svb.com")
        funding_round = FundingRound(startup=startup)
        with self.assertRaises(Exception):
            funding_round.startup = Startup(name="ftx", founder="sbf", domain="ftx.com")
        Startup.all = []
        VentureCapitalist.all = []
        FundingRound.all = []
        
    def test_has_venture_capitalist(self):
        venture_capitalist = VentureCapitalist(name="Ren", total_worth=3000000)
        funding_round = FundingRound(venture_capitalist=venture_capitalist)
        self.assertEqual(venture_capitalist, funding_round.venture_capitalist)
        Startup.all = []
        VentureCapitalist.all = []
        FundingRound.all = []
        
    def test_venture_capitalist_is_immutable(self):
        venture_capitalist = VentureCapitalist(name="Ren", total_worth=3000000)
        funding_round = FundingRound(venture_capitalist=venture_capitalist)
        with self.assertRaises(Exception):
            funding_round.venture_capitalist = VentureCapitalist(name="Ryan", total_worth=3000000)
        Startup.all = []
        VentureCapitalist.all = []
        FundingRound.all = []
        
    def test_returns_funding_round_type(self):
        startup = Startup(name="svb", founder="Greg Becker", domain="svb.com")
        venture_capitalist = VentureCapitalist(name="Ren", total_worth=3000000)
        funding_round = FundingRound(venture_capitalist=venture_capitalist, 
                                     startup=startup, 
                                     type_="Angel")
        self.assertEqual(funding_round.type_, "Angel")
        Startup.all = []
        VentureCapitalist.all = []
        FundingRound.all = []
        
    def test_returns_investement(self):
        startup = Startup(name="svb", founder="Greg Becker", domain="svb.com")
        venture_capitalist = VentureCapitalist(name="Ren", total_worth=3000000)
        funding_round = FundingRound(venture_capitalist=venture_capitalist, 
                                     startup=startup, 
                                     type_="Angel",
                                     investement=481924.123)
        self.assertEqual(funding_round.investement, 481924.123)
        Startup.all = []
        VentureCapitalist.all = []
        FundingRound.all = []
        
    def test_investement_is_positive_float(self):
        startup = Startup(name="svb", founder="Greg Becker", domain="svb.com")
        venture_capitalist = VentureCapitalist(name="Ren", total_worth=3000000)
        with self.assertRaises(Exception):
            FundingRound(venture_capitalist=venture_capitalist, 
                                        startup=startup, 
                                        type_="Angel",
                                        investement=-481924.123)
        Startup.all = []
        VentureCapitalist.all = []
        FundingRound.all = []
        
    def test_returns_all_rounds(self):
        startup = Startup(name="svb", founder="Greg Becker", domain="svb.com")
        startup1 = Startup(name="ftx", founder="sbf", domain="ftx.com")
        venture_capitalist = VentureCapitalist(name="Ryan", total_worth=3000000) 
        venture_capitalist1 = VentureCapitalist(name="Ren", total_worth=3000000)
        funding_round = FundingRound(venture_capitalist=venture_capitalist, 
                                     startup=startup, 
                                     type_="Angel",
                                     investement=481924.123)
        funding_round1 = FundingRound(venture_capitalist=venture_capitalist1, 
                                     startup=startup1, 
                                     type_="Series A",
                                     investement=481924.123)
        self.assertCountEqual([funding_round, funding_round1], FundingRound.all)
        Startup.all = []
        VentureCapitalist.all = []
        FundingRound.all = []