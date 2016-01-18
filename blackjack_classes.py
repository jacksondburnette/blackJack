#!/usr/bin/env python
"""Classes to be used in blackJack game"""

from random import shuffle

class Player(object):

    def __init__(self,human=True,bankroll=0,busted=False,is_turn=False):
        self.human = human
        self.bankroll = bankroll
        self.busted = busted
        self.is_turn = is_turn

    def bankroll_add(self,value):
        """Return players bankroll with value added"""
        self.bankroll += value
        return self.bankroll

    def bankroll_sub(self,value):
        """Return players bankroll with value subtracted"""
        self.bankroll -= value
        return self.bankroll

    def bet(self,value):
        """allow player to bet value
        Return tuple (bet,updated bankroll)"""
        bet = value
        self.bankroll = self.bankroll_sub(value)
        return (bet,self.bankroll)

    def move(self,choice):
        """choice = hit or stay (split TBD)"""
        done = False
        while not done:
            if(choice == 'hit'):
                print 'Hit me!'
                done = True
            elif(choice == 'stay'):
                print 'Stay'
                done = True
            else:
                print 'Not a valid move, try again.'

class Card(object):

    int_values = {
        '1':1, '2':2, '3':3,
        '4':4, '5':5, '6':6,
        '7':7, '8':8, '9':9,
        '10':10, 'J':10, 'Q':10,
        'K':10, 'low_A':1, 'high_A':11
    }

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank

    def get_rank(self):
        """Return rank of card object as string 1-10, J, Q, K, low_A or high_A"""
        return self.rank

    def get_suit(self):
        """Return suit or card object as string H=Heart, C=Club,
        D=Diamond, S=Spade"""
        return self.suit

    def int_value(self):
        """assign integer value to card object based on blackjack rules
        (i.e. numerical card = number, face cards = 10, low_A = 1, high_A = 11"""
        return int_values[self.get_rank]

class Deck(object):

    def __init__(self,
                 suits=['H','C','D','S'],
                 ranks=['1','2','3','4','5','6','7',
                        '8','9','10','J','Q','K','A'],
                 contents=[]
                ):
        self.suits = suits
        self.ranks = ranks
        self.contents = contents

    def make_deck(self):
        """makes standard 52 card deck"""
        for suits in self.suits:
            for rank in self.ranks:
                self.contents.append(Card(suit,rank))

    def add_card(self,card):
        """add card object to deck contents"""
        self.contents = self.contents.append(card)
        return self.contents

    def sub_card(self,card):
        """remove card object from deck contents"""
        self.contents.remove(card)
        return self.contents

    def shuffle(self):
        """returns contents of deck, shuffled"""
        shuffle(self.contents)
        return self.contents
