import unittest
from funding_round import FundingRound
from venture_capitalist import VentureCapitalist
from startup import Startup

class Venture_Capitalist_Test(unittest.TestCase):
    def test_has_name(self):
        venture_capitalist = VentureCapitalist(name="Ryan")
        self.assertEqual(venture_capitalist.name, "Ryan")
        Startup.all = []
        VentureCapitalist.all = []
        FundingRound.all = []
        
    def test_has_capital(self):
        venture_capitalist = VentureCapitalist(total_worth=3000000)
        self.assertEqual(venture_capitalist.total_worth, 3000000)
        Startup.all = []
        VentureCapitalist.all = []
        FundingRound.all = []
        
    def test_all_list(self):
        venture_capitalist = VentureCapitalist(name="Ryan", total_worth=3000000)
        venture_capitalist1 = VentureCapitalist(name="Ren", total_worth=3000000)
        self.assertCountEqual([venture_capitalist, venture_capitalist1], VentureCapitalist.all)
        Startup.all = []
        VentureCapitalist.all = []
        FundingRound.all = []
        
    def test_tres_commas_club(self):
        venture_capitalist = VentureCapitalist(name="Ryan", total_worth=2000000000)
        venture_capitalist1 = VentureCapitalist(name="Ren", total_worth=2000000000)
        VentureCapitalist(name="Historia", total_worth=3000000)
        self.assertCountEqual([venture_capitalist, venture_capitalist1], 
                              VentureCapitalist.tres_commas_club())
        Startup.all = []
        VentureCapitalist.all = []
        FundingRound.all = []
    
    def test_offer_contract(self):
        startup = Startup(name="svb", founder="Greg Becker", domain="svb.com")
        venture_capitalist = VentureCapitalist(name="Ryan", total_worth=2000000000)
        venture_capitalist.offer_contract(startup=startup,
                                          investement=481924.00,
                                          type_="Angel")
        self.assertIn(venture_capitalist, [venture.venture_capitalist for venture in FundingRound.all])
        
        Startup.all = []
        VentureCapitalist.all = []
        FundingRound.all = []
    
    def test_funding_rounds(self):
        startup = Startup(name="svb", founder="Greg Becker", domain="svb.com")
        startup1 = Startup(name="ftx", founder="sbf", domain="ftx.com")
        venture_capitalist = VentureCapitalist(name="Ryan", total_worth=3000000) 
        venture_capitalist1 = VentureCapitalist(name="Ren", total_worth=3000000)
        funding_round = FundingRound(venture_capitalist=venture_capitalist, 
                                     startup=startup, 
                                     type_="Angel",
                                     investement=481924.123)
        funding_round1 = FundingRound(venture_capitalist=venture_capitalist, 
                                     startup=startup1, 
                                     type_="Series A",
                                     investement=481924.123)
        funding_round2 = FundingRound(venture_capitalist=venture_capitalist1, 
                                     startup=startup1, 
                                     type_="Series A",
                                     investement=481924.123)
        
        self.assertCountEqual([funding_round, funding_round1], venture_capitalist.funding_rounds())
        
        Startup.all = []
        VentureCapitalist.all = []
        FundingRound.all = []
        
    def test_portfolio(self):
        startup = Startup(name="svb", founder="Greg Becker", domain="svb.com")
        startup1 = Startup(name="ftx", founder="sbf", domain="ftx.com")
        venture_capitalist = VentureCapitalist(name="Ryan", total_worth=3000000) 
        FundingRound(venture_capitalist=venture_capitalist, 
                                     startup=startup, 
                                     type_="Angel",
                                     investement=481924.123)
        FundingRound(venture_capitalist=venture_capitalist, 
                                     startup=startup1, 
                                     type_="Series A",
                                     investement=481924.123)
        FundingRound(venture_capitalist=venture_capitalist, 
                                     startup=startup1, 
                                     type_="Series C",
                                     investement=481924.123)
        
        self.assertCountEqual([startup, startup1], venture_capitalist.portfolio())
    
    def test_return_biggest_investement(self):
        startup = Startup(name="svb", founder="Greg Becker", domain="svb.com")
        startup1 = Startup(name="ftx", founder="sbf", domain="ftx.com")
        venture_capitalist = VentureCapitalist(name="Ryan", total_worth=3000000) 
        funding_round = FundingRound(venture_capitalist=venture_capitalist, 
                                     startup=startup, 
                                     type_="Angel",
                                     investement=5152512)
        funding_round1 = FundingRound(venture_capitalist=venture_capitalist, 
                                     startup=startup1, 
                                     type_="Series A",
                                     investement=481924.00)
        funding_round2 = FundingRound(venture_capitalist=venture_capitalist, 
                                     startup=startup1, 
                                     type_="Series C",
                                     investement=481924.123)
        
        self.assertEqual(funding_round, venture_capitalist.biggest_investement())
    
    def test_return_invested_domain(self):
        startup = Startup(name="svb", founder="Greg Becker", domain="svb.com")
        startup1 = Startup(name="ftx", founder="sbf", domain="ftx.com")
        venture_capitalist = VentureCapitalist(name="Ryan", total_worth=3000000) 
        FundingRound(venture_capitalist=venture_capitalist, 
                                     startup=startup, 
                                     type_="Angel",
                                     investement=5152512)
        FundingRound(venture_capitalist=venture_capitalist, 
                                     startup=startup1, 
                                     type_="Series A",
                                     investement=481924.00)
        FundingRound(venture_capitalist=venture_capitalist, 
                                     startup=startup1, 
                                     type_="Series C",
                                     investement=481924.123)
        
        self.assertEqual(963848.123, venture_capitalist.invested("ftx.com"))