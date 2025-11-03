#!/usr/bin/env python3

import random
import statistics

class Event:

  def __init__(self, win, loss, tie):
    self.outcome_win = _Event_Odds(win)
    self.outcome_loss = _Event_Odds(loss)
    self.outcome_tie = _Event_Odds(tie)

  def __repr__(self):
    return f"Event=Win:{self.outcome_win};Lose:{self.outcome_loss};({self.outcome_win._bet_pay:.2f},{self.outcome_loss._bet_pay:.2f})({self.outcome_win._percent:.2f},{self.outcome_loss._percent:.2f})"

  def get_american_win_p(self):
    return self.outcome_win._american_positive

  def get_american_loss_p(self):
    return self.outcome_loss._american_positive

  def get_american_win_n(self):
    return self.outcome_win._american_negitive

  def get_american_loss_n(self):
    return self.outcome_loss._american_negitive

class _Event_Odds:

  def __init__(self, percent):
    self._percent = percent
    self._american_negitive = statistics.calculate_american_negitive(percent)
    self._american_positive = statistics.calculate_american_positive(percent)
    self._bet_pay = self._calculate_pay()

  def get_bet_pay(self):
    return self._bet_pay

  def _calculate_pay(self):
    odds = self.get_book_odds_repr()
    if(self._percent < .5):
      amt = abs(odds)
    else:
      amt = 100 * 100 / abs(odds)
    return amt

  def get_book_odds_repr(self):
    odds = None
    if(self._percent < .5):
      odds = self._american_positive
    else:
      odds = self._american_negitive
    return odds

  def __repr__(self):
    return str(self.get_book_odds_repr())
