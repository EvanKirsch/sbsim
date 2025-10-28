#!/usr/bin/env python3

import random
import math
from odds import *

class Abstract_Book:
  pass



class Baseline_Book(Abstract_Book):

  def __init__(self):
    self.odds = []


  def generate_book(self, size):
    for i in range(size):
      event_a = random.randint(20,80)/100
      event_b = 1-event_a
      self.odds.append([event_a, event_b])



class Book(Abstract_Book):

  def __init__(self, baseline_book):
    self.softness = random.random()
    self.book_odds = self.generate_book_odds(baseline_book.odds)


  def generate_book_odds(self, baseline_odds):
    tmp_book_odds = []
    for event_odds in baseline_odds:
      tmp_event = self.get_event(event_odds)
      tmp_book_odds.append(tmp_event)
    return tmp_book_odds


  def get_event(self, event_odds):
    odds = []
    odds_event_a = None
    odds_event_b = None
    varriation = random.random()
    over_under = random.randint(0,1)
    varriation_adjustment = varriation / (self.softness * 100)
    if(over_under == 0):
      odds_event_a = event_odds[0] + varriation_adjustment
      odds_event_b = event_odds[1] - varriation_adjustment
    else:
      odds_event_a = event_odds[0] - varriation_adjustment
      odds_event_b = event_odds[1] + varriation_adjustment
    possible_event_odds = [Odds(odds_event_a), Odds(odds_event_b), Odds(0.002)]

    return Event(possible_event_odds)
