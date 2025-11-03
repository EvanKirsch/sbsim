#!/usr/bin/env python3

def calculate_market_margin(bet_win_odds, bet_loss_odds):
    dc_bet_win_odds = calculate_decimal_odds(bet_win_odds)
    dc_bet_loss_odds = calculate_decimal_odds(bet_loss_odds)
    return dc_bet_win_odds + dc_bet_loss_odds

### Odds Conversions

def calculate_american_negitive(percent):
    return round(((percent*100) / (1 - percent)) * -1)

def calculate_american_positive(percent):
    return round((100 / percent) - 100)

def calculate_decimal_odds(american_odds):
    dc_odds = 0
    if(american_odds > 0):
        dc_odds = 100 / (american_odds + 100)
    else:
        dc_odds = abs(american_odds) / (abs(american_odds) + 100)
    return dc_odds
