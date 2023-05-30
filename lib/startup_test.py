import unittest
from funding_round import FundingRound
from venture_capitalist import VentureCapitalist
from startup import Startup
 
class Startup_test(unittest.TestCase):
    def setUp(self) -> None:
        startup = Startup(name="svb", founder="Greg Becker", domain="svb.com")
        startup1 = Startup(name="ftx", founder="sbf", domain="ftx.com")
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
        return super().setUp()
    
    def tearDown(self) -> None:
        Startup.all = []
        VentureCapitalist.all = []
        FundingRound.all = [] 
        return super().tearDown()
    
    def test_has_name(self):
        self.assertEqual(self.startup.name, "svb")
        
    def test_name_is_str(self):
        with self.assertRaises(Exception):
            Startup(name=None)
        
    def test_has_founder(self):
        self.assertEqual(self.startup.founder, "Greg Becker")
        
    def test_founder_is_str(self):
        with self.assertRaises(Exception):
            Startup(founder=None)
        
    def test_founder_is_immutable(self):
        with self.assertRaises(Exception):
            self.startup.founder = "Banckrupt"
  
    def test_has_domain(self):
        self.assertEqual(self.startup.domain, "svb.com")
        
    def test_domain_is_immutable(self):
        with self.assertRaises(Exception):
            self.startup.domain = "svnb.com"
        
    def test_pivot(self):
        self.startup.pivot(name="ftx", domain="ftx.com")
        self.assertEqual(self.startup.name, "ftx")
        self.assertEqual(self.startup.domain, "ftx.com")
        
    def test_all_list(self):
        self.assertCountEqual([self.startup, self.startup1], Startup.all)
        
    def test_find_by_founder(self):
        self.assertEqual(self.startup1, Startup.find_by_founder("sbf"))
    
    def test_domains(self):
        self.assertCountEqual(["svb.com", "ftx.com"], Startup.domains)
        
    def test_sign_contract(self):
        self.assertIn(self.startup, FundingRound.all)

               
    def test_returns_num_rounds(self):
        self.assertEqual(self.startup.num_funding_rounds(), 2)
         
    def test_total_funds(self):
        self.assertEqual(self.startup.total_funds(), 963848.00)
        
    def test_returns_unique_investors(self):
        self.assertCountEqual([self.venture_capitalist, self.venture_capitalist1], self.startup.investors())
        
    def test_returns_big_investors(self):
        self.assertCountEqual([self.venture_capitalist], self.startup.big_investors())
        