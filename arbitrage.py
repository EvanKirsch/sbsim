#!/usr/bin/env python3

from book import Book

def find_arbitrages(event_ids, my_books):
    arbitrages = {}
    for event_id in event_ids:
        arbitrages[event_id] = Arbitrage(event_id)

        for my_book in my_books:
            my_event = my_book.book_odds[event_id]

            win_payout = my_event.outcome_win.get_bet_pay()
            if(win_payout > abs(arbitrages[event_id].max_win_payout)):
                arbitrages[event_id].max_win_payout_book_id = my_book.book_id
                arbitrages[event_id].max_win_payout = win_payout
                arbitrages[event_id].max_win_odds = my_event.outcome_win.get_book_odds_repr()

            loss_payout = my_event.outcome_loss.get_bet_pay()
            if(loss_payout > arbitrages[event_id].max_loss_payout):
                arbitrages[event_id].max_loss_payout_book_id = my_book.book_id
                arbitrages[event_id].max_loss_payout = loss_payout
                arbitrages[event_id].max_loss_odds = my_event.outcome_loss.get_book_odds_repr()

    return arbitrages


class Arbitrage:

  def __init__(self, event_id):
    self.event_id = event_id
    self.max_win_payout_book_id = None
    self.max_win_payout = 0
    self.max_win_odds = None
    self.max_loss_payout_book_id = None
    self.max_loss_payout = 0
    self.max_loss_odds = None

  def __repr__(self):
    event_win = self._f_uuid(self.max_win_payout_book_id)
    event_loss = self._f_uuid(self.max_loss_payout_book_id)
    roi = self._calculate_roi(self.max_win_odds, self.max_loss_odds)
    # win_bet = self._calculate_bet(self.max_win_odds)
    # loss_bet = self._calculate_bet(self.max_loss_odds)
    return f"{(roi*100):.1f}({event_win}:{self.max_win_odds}),({event_loss}:{self.max_loss_odds})"

  def _f_uuid(self, uuid):
    x = str(uuid.int)
    return f"{x[:4]}"

  def _calculate_roi(self, bet_win_odds, bet_loss_odds):
      dc_bet_win_odds = self._calculate_decimal_odds(bet_win_odds)
      dc_bet_loss_odds = self._calculate_decimal_odds(bet_loss_odds)
      print(dc_bet_win_odds, dc_bet_loss_odds)
      return 1-(dc_bet_win_odds + dc_bet_loss_odds)

  def _calculate_decimal_odds(self, american_odds):
      dc_odds = 0
      if(american_odds > 0):
        dc_odds = 100 / (american_odds + 100)
      else:
        dc_odds = abs(american_odds) / (abs(american_odds) + 100)
      return dc_odds
