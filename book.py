#!/usr/bin/env python3

import random
import math
import uuid
from event import Event

class Baseline_Book:

  def __init__(self):
    self.odds = {}

  def generate_book(self, size):
    for i in range(size):
      event_a = random.randint(20,80)/100
      event_b = 1-event_a
      event_id = uuid.uuid4()
      self.odds[event_id] = [event_a, event_b]


class Book:

  def __init__(self, baseline_book):
    self.softness = random.random()
    self.book_odds = self.generate_book_odds(baseline_book.odds)
    self.book_id = uuid.uuid4()

  def __repr__(self):
    x = str(self.book_id.int)
    return f"{x[:4]}:{self.book_odds}"

  def generate_book_odds(self, baseline_odds):
    tmp_book_odds = {}
    for event_id in baseline_odds.keys():
      tmp_event = self.get_event(baseline_odds[event_id])
      tmp_book_odds[event_id] = tmp_event
    return tmp_book_odds


  def get_event(self, event_odds):
    odds = []
    odds_event_a = None
    odds_event_b = None
    varriation = random.randint(0,30) / 100
    over_under = random.randint(0,1)
    #TODO - bad
    varriation_adjustment = varriation / (self.softness * 100)
    if(over_under == 0):
      odds_event_a = event_odds[0] + varriation_adjustment
      odds_event_b = event_odds[1] - varriation_adjustment
    else:
      odds_event_a = event_odds[0] - varriation_adjustment
      odds_event_b = event_odds[1] + varriation_adjustment
    return Event(odds_event_a, odds_event_b, 0.002)
