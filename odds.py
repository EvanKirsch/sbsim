#!/usr/bin/env python3
import random

class Odds:

    def __init__(self):
       self.percent = None
       self.fzy_american_negitive = None
       self.fzy_american_positive = None

    def __init__(self, percent):
       self.percent = percent
       self.fzy_american_negitive = self.get_american_negitive()
       self.fzy_american_positive = self.get_american_positive()

    def get_american_negitive(self):
        fuzz = random.randint(-5,5)/100
        return (((self.percent+fuzz)*100) / (1 - (self.percent+fuzz))) * -1

    def get_american_positive(self):
        fuzz = random.randint(-5,5)/100
        return (100 / (self.percent+fuzz)) - 100

    def __repr__(self):
        str_repr = ""
        if(abs(self.fzy_american_positive) > abs(self.fzy_american_negitive)):
            str_repr = str(round(self.fzy_american_positive))
        else:
            str_repr = str(round(self.fzy_american_negitive))
        return str_repr

class Event:

    def __init__(self):
        self.outcome_win = None
        self.outcome_loose = None
        self.outcome_tie = None

    def __init__(self, odds):
        self.outcome_win = odds[0]
        self.outcome_loose = odds[1]
        self.outcome_tie = odds[2]

    def __repr__(self):
        return f"\nEvent=Win:{self.outcome_win};Lose:{self.outcome_loose};({self.outcome_win.percent:.2f},{self.outcome_loose.percent:.2f})"
