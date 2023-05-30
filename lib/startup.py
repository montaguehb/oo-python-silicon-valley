#!/usr/bin/env python3

from funding_round import FundingRound

class Startup:
   all=[]
   
   def __init__(self, name, founder, domain):
      self.name = name
      if isinstance(founder, str):
         self._founder = founder
      else:
         raise AttributeError
      self._domain = domain
      Startup.all.append(self)
      
   @property
   def founder(self):
      return self._founder
   
   @founder.setter
   def founder(self, founder):
      raise AttributeError
   
   @property
   def name(self):
      return self._name
   
   @name.setter
   def name(self, name):
      if isinstance(name, str):
         self._name = name
      else:
         raise AttributeError
   
   @property
   def domain(self):
      return self._domain
   
   @domain.setter
   def domain(self, domain):
      raise AttributeError
   
   def pivot(self, domain, name):
      self.name = name
      self._domain = domain
   
   @classmethod
   def find_by_founder(cls, founder):
      return [startup for startup in cls.all if startup.founder == founder]
   
   @classmethod
   def domains(cls):
      return [startup.domain for startup in cls.all]