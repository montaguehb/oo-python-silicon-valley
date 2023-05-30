import unittest
from funding_round import FundingRound
from venture_capitalist import VentureCapitalist
from startup import Startup

class Founding_Round_Test(unittest.TestCase):
    def setUp(self) -> None:
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
        return super().setUp()
    
    def tearDown(self) -> None:
        Startup.all = []
        VentureCapitalist.all = []
        FundingRound.all = []
        return super().tearDown()
    
    def test_has_startup(self):
        self.assertEqual(self.startup, self.funding_round.startup)

        
    def test_startup_is_immutable(self):
        with self.assertRaises(Exception):
            self.funding_round.startup = Startup(name="ftx", founder="sbf", domain="ftx.com")
        
    def test_has_venture_capitalist(self):
        self.assertEqual(self.venture_capitalist, self.funding_round.venture_capitalist)
        
    def test_venture_capitalist_is_immutable(self):
        with self.assertRaises(Exception):
            self.funding_round.venture_capitalist = VentureCapitalist(name="Ryan", total_worth=3000000)
        
    def test_returns_funding_round_type(self):
        self.assertEqual(self.funding_round.type_, "Angel")
        
    def test_returns_investement(self):
        self.assertEqual(self.funding_round.investement, 481924.123)
        
    def test_investement_is_positive_float(self):
        with self.assertRaises(Exception):
            FundingRound(venture_capitalist=self.venture_capitalist, 
                                        startup=self.startup, 
                                        type_="Angel",
                                        investement=-481924.123)
        
    def test_returns_all_rounds(self):
        self.assertCountEqual([self.funding_round, self.funding_round1], FundingRound.all)