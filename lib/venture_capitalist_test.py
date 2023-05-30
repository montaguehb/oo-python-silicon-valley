import unittest
from funding_round import FundingRound
from venture_capitalist import VentureCapitalist
from startup import Startup

class Venture_Capitalist_Test(unittest.TestCase):
    def setUp(self) -> None:
        try:
            self.startup = Startup(name="svb", founder="Greg Becker", domain="svb.com")
            self.startup1 = Startup(name="ftx", founder="sbf", domain="ftx.com")
        except Exception as e:
            print(e)
        self.venture_capitalist_ryan = VentureCapitalist(name="Ryan", total_worth=3000000)
        self.venture_capitalist_ren = VentureCapitalist(name="Ren", total_worth=3000000)
        self.venture_capitalist_tres = VentureCapitalist(name="Historia", total_worth=2000000000) 
        try:     
            self.funding_round = FundingRound(venture_capitalist=self.venture_capitalist_ryan, 
                                        startup=self.startup, 
                                        type_="Angel",
                                        investement=5152512)
            self.funding_round1 = FundingRound(venture_capitalist=self.venture_capitalist_ryan, 
                                        startup=self.startup1, 
                                        type_="Series A",
                                        investement=481924.00)
            self.funding_round2 = FundingRound(venture_capitalist=self.venture_capitalist_ren, 
                                        startup=self.startup1, 
                                        type_="Series C",
                                        investement=481924.123)
        except Exception as e:
            print(e)
        return super().setUp()
    
    def tearDown(self) -> None:
        Startup.all = []
        VentureCapitalist.all = []
        FundingRound.all = []
        return super().tearDown()
    
    def test_has_name(self):
        self.assertEqual(self.venture_capitalist_ryan.name, "Ryan")
    
    def test_name_is_str(self):
        with self.assertRaises(Exception):
            VentureCapitalist(name=3, total_worth=58134142)
            
    def test_has_capital(self):
        self.assertEqual(self.venture_capitalist_ryan.total_worth, 3000000)
    
    def test_total_worth_is_float(self):
        with self.assertRaises(Exception):
            self.venture_capitalist_ren.total_worth = "test"
                
    def test_all_list(self):
        self.assertCountEqual([self.venture_capitalist_ryan, self.venture_capitalist_ren, self.venture_capitalist_tres], VentureCapitalist.all)
        
    def test_tres_commas_club(self):
        self.assertCountEqual([self.venture_capitalist_tres], 
                              VentureCapitalist.tres_commas_club())
    
    def test_offer_contract(self):
        self.venture_capitalist_ryan.offer_contract(startup=self.startup,
                                                    investement=481924.00,
                                                    type_="Angel")
        self.assertIn(self.venture_capitalist_ryan, [venture.venture_capitalist for venture in FundingRound.all])
    
    def test_funding_rounds(self):
        self.assertCountEqual([self.funding_round, self.funding_round1], self.venture_capitalist_ryan.funding_rounds())
        
    def test_portfolio(self):
        self.assertCountEqual([self.startup, self.startup1], self.venture_capitalist_ryan.portfolio())
    
    def test_return_biggest_investement(self):
        self.assertEqual(self.funding_round, self.venture_capitalist_ryan.biggest_investement())
    
    def test_return_invested_domain(self):
        self.assertEqual(963848.00, self.venture_capitalist_ryan.invested("ftx.com"))