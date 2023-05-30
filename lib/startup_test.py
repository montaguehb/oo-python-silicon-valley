import unittest
from funding_round import FundingRound
from venture_capitalist import VentureCapitalist
from startup import Startup
 
class Startup_test(unittest.TestCase):
    def test_has_name(self):
        startup = Startup(name="svb")
        self.assertEqual(startup.name, "svb")
        Startup.all = []
        
    def test_name_is_str(self):
        with self.assertRaises(Exception):
            Startup(name=None)
        Startup.all = []
        
    def test_has_founder(self):
        startup = Startup(founder="Greg Becker")
        self.assertEqual(startup.founder, "Greg Becker")
        Startup.all = []
        
    def test_founder_is_str(self):
        with self.assertRaises(Exception):
            Startup(founder=None)
        Startup.all = []
        
    def test_founder_is_immutable(self):
        startup = Startup(founder="Greg Becker")
        with self.assertRaises(Exception):
            startup.founder = "Banckrupt"
        Startup.all = []
        
    def test_has_domain(self):
        startup = Startup(domain="svb.com")
        self.assertEqual(startup.domain, "svb.com")
        Startup.all = []
        
    def test_domain_is_immutable(self):
        startup = Startup(domain="svb.com")
        with self.assertRaises(Exception):
            startup.domain = "svnb.com"
        Startup.all = []
        
    def test_pivot(self):
        startup = Startup(name="svb", founder="Greg Becker", domain="svb.com")
        startup.pivot(name="ftx", domain="ftx.com")
        self.assertEqual(startup.name, "ftx")
        self.assertEqual(startup.domain, "ftx.com")
        Startup.all = []
        
    def test_all_list(self):
        startup = Startup(name="svb", founder="Greg Becker", domain="svb.com")
        startup1 = Startup(name="ftx", founder="sbf", domain="ftx.com")
        
        self.assertCountEqual([startup, startup1], Startup.all)
        Startup.all = []
        
    def test_find_by_founder(self):
        Startup(name="svb", founder="Greg Becker", domain="svb.com")
        startup1 = Startup(name="ftx", founder="sbf", domain="ftx.com")      

        self.assertEqual(startup1, Startup.find_by_founder("sbf"))
        Startup.all = []
    
    def test_domains(self):
        Startup(name="svb", founder="Greg Becker", domain="svb.com")
        Startup(name="ftx", founder="sbf", domain="ftx.com") 
        
        self.assertCountEqual(["svb.com", "ftx.com"], Startup.domains)
        Startup.all = []
        
    def test_sign_contract(self):
        startup = Startup(name="svb", founder="Greg Becker", domain="svb.com")
        venture_capitalist = VentureCapitalist(name="Ren", total_worth=3000000)
        startup.sign_contract(venture_capitalist=venture_capitalist,
                              type_="Angel",
                              investement=481924.00)
        self.assertIn(startup, FundingRound.all)
        Startup.all = []
        VentureCapitalist.all = []
        FundingRound.all = [] 
               
    def test_returns_num_rounds(self):
        startup = Startup(name="svb", founder="Greg Becker", domain="svb.com")
        venture_capitalist = VentureCapitalist(name="Ren", total_worth=3000000)
        venture_capitalist1 = VentureCapitalist(name="Ryan", total_worth=3000000)
        startup.sign_contract(venture_capitalist=venture_capitalist,
                              type_="Angel",
                              investement=481924.00)
        startup.sign_contract(venture_capitalist=venture_capitalist1,
                              type_="Angel",
                              investement=481924.00)
        self.assertEqual(startup.num_funding_rounds(), 2)
        Startup.all = []
        VentureCapitalist.all = []
        FundingRound.all = []
         
    def test_total_funds(self):
        startup = Startup(name="svb", founder="Greg Becker", domain="svb.com")
        venture_capitalist = VentureCapitalist(name="Ren", total_worth=3000000)
        venture_capitalist1 = VentureCapitalist(name="Ryan", total_worth=3000000)
        startup.sign_contract(venture_capitalist=venture_capitalist,
                              type_="Angel",
                              investement=481924.00)
        startup.sign_contract(venture_capitalist=venture_capitalist1,
                              type_="Angel",
                              investement=481924.00)
        
        self.assertEqual(startup.total_funds(), 963848.00)
        Startup.all = []
        VentureCapitalist.all = []
        FundingRound.all = [] 
        
    def test_returns_unique_investors(self):
        startup = Startup(name="svb", founder="Greg Becker", domain="svb.com")
        venture_capitalist = VentureCapitalist(name="Ren", total_worth=3000000)
        venture_capitalist1 = VentureCapitalist(name="Ryan", total_worth=3000000)
        startup.sign_contract(venture_capitalist=venture_capitalist,
                              type_="Angel",
                              investement=481924.00)
        startup.sign_contract(venture_capitalist=venture_capitalist,
                              type_="Series A",
                              investement=481924.00)
        startup.sign_contract(venture_capitalist=venture_capitalist1,
                              type_="Angel",
                              investement=481924.00)
        
        self.assertCountEqual([venture_capitalist, venture_capitalist1], startup.investors())
        Startup.all = []
        VentureCapitalist.all = []
        FundingRound.all = [] 
        
    def test_returns_big_investors(self):
        startup = Startup(name="svb", founder="Greg Becker", domain="svb.com")
        venture_capitalist = VentureCapitalist(name="Ren", total_worth=2000000000)
        venture_capitalist1 = VentureCapitalist(name="Ryan", total_worth=3000000)
        startup.sign_contract(venture_capitalist=venture_capitalist,
                              type_="Angel",
                              investement=481924.00)
        startup.sign_contract(venture_capitalist=venture_capitalist,
                              type_="Series A",
                              investement=481924.00)
        startup.sign_contract(venture_capitalist=venture_capitalist1,
                              type_="Angel",
                              investement=481924.00)
        
        self.assertCountEqual([venture_capitalist], startup.big_investors())
        Startup.all = []
        VentureCapitalist.all = []
        FundingRound.all = []
        