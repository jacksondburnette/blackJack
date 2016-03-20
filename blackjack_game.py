#!/usr/bin/env python

import pdb
import blackjack_classes as blackjack

def play_blackjack():
    deck = blackjack.Deck()
    deck.make_deck()
    deck.shuffle()

    game = blackjack.Game()
    game.meet_players()

    #the house is always the first Player in player list
    house = game.players[0]
    game_on = True
    while game_on:
        game.initial_bets()
        game.deal_cards(deck)
        #pdb.set_trace()
        game.players_move(deck)
        game.house_move(house,deck)
        game.payout()
        game.cleanup()

        game.remove_players()
        game_on = game.check_done()

play_blackjack()
