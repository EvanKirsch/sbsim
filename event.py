#!/usr/bin/env python3

import random

class Event:

    def __init__(self):
        self.outcome_win = None
        self.outcome_loose = None
        self.outcome_tie = None

    def __init__(self, win, loose, tie):
        self.outcome_win = _Event_Odds(win)
        self.outcome_loose = _Event_Odds(loose)
        self.outcome_tie = _Event_Odds(tie)

    def __repr__(self):
        return f"Event=Win:{self.outcome_win};Lose:{self.outcome_loose};({self.outcome_win._percent:.2f},{self.outcome_loose._percent:.2f})"



class _Event_Odds:

    def __init__(self):
       self._percent = None
       self._fzy_american_negitive = None
       self._fzy_american_positive = None

    def __init__(self, percent):
       self._percent = percent
       self._fzy_american_negitive = self._calculate_american_negitive()
       self._fzy_american_positive = self._calculate_american_positive()

    def _calculate_american_negitive(self):
        fuzz = random.randint(-5,5)/100
        return (((self._percent + fuzz)*100) / (1 - (self._percent + fuzz))) * -1

    def _calculate_american_positive(self):
        fuzz = random.randint(-5,5)/100
        return (100 / (self._percent + fuzz)) - 100

    def __repr__(self):
        str_repr = ""
        if(self._percent < .5):
            str_repr = str(round(self._fzy_american_positive))
        else:
            str_repr = str(round(self._fzy_american_negitive))
        return str_repr
