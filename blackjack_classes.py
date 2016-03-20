#!/usr/bin/env python
"""Classes to be used in blackJack game"""

from random import shuffle
import pdb

class Card(object):

    #A=1 by default
    int_values = {
        '2':2, '3':3,
        '4':4, '5':5, '6':6,
        '7':7, '8':8, '9':9,
        '10':10, 'J':10, 'Q':10,
        'K':10, 'low_A':1, 'high_A':11,
        'A':1
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
        return self.int_values[self.get_rank()]

class Deck(object):

    def __init__(self,
                 suits=['H','C','D','S'],
                 ranks=['2','3','4','5','6','7',
                        '8','9','10','J','Q','K','A'],
                 contents=[]
                ):
        self.suits = suits
        self.ranks = ranks
        self.contents = contents

    def make_deck(self):
        """makes standard 52 card deck"""
        for suit in self.suits:
            for rank in self.ranks:
                self.contents.append(Card(suit,rank))

    def add_card(self,card):
        """add card object to deck contents"""
        self.contents.append(card)

    def sub_card(self,card):
        """remove card object from deck contents"""
        self.contents.remove(card)

    def top_card(self):
        """return top card object in deck"""
        return self.contents[0]

    def shuffle(self):
        """returns contents of deck, shuffled"""
        shuffle(self.contents)

class Hand(object):

    def __init__(self, contents=0):
        if not contents:
            self.contents = []

    def add_card(self,card):
        """add card object to hand contents"""
        self.contents.append(card)

    def sub_card(self,card):
        """remove card object from deck contents"""
        self.contents.remove(card)

    def deal(self,deck,num_cards=2):
         """make blackjack hand with given size (2 in blackjack) from deck object"""
         i = 0
         while i < num_cards:
             #move card from deck to hand
             self.add_card(deck.top_card())
             deck.sub_card(deck.top_card())
             i += 1

    def show(self):
        """show cards in hand"""
        for card in self.contents:
            print card.rank + ' of ' + card.suit

    def value(self):
        val = 0
        for card in self.contents:
            val += card.int_value()
        return val

class Player(object):

    def __init__(self,name,bet=0,hand=0,human=True,bankroll=1000,
                 busted=False,is_turn=False):
        self.human = human
        self.bet = bet
        self.bankroll = bankroll
        self.busted = busted
        self.is_turn = is_turn
        self.name = name
        if not hand:
            self.hand = Hand()

    def bankroll_add(self,value):
        """Return players bankroll with value added"""
        self.bankroll += value

    def bankroll_sub(self,value):
        """Return players bankroll with value subtracted"""
        self.bankroll -= value

    def make_bet(self,value):
        """allow player to bet value
        subtract value from bankroll, return value"""
        self.bankroll_sub(value)
        return value

    def hit(self,deck):
        """deal 1 card from deck object"""
        self.hand.deal(deck,1)

    def stay(self):
        pass

    def double(self,bet):
        """double players existing bet"""
        self.bet(bet)

    def move(self,deck):
        """choice = hit or stay (split TBD)"""
        #pdb.set_trace()
        choice = raw_input('Your move: ')
        done = False
        while not done:
            if(choice == 'hit'):
                self.hit(deck)
                print 'Hit me!'
                self.hand.show()
                if self.hand.value() > 21:
                    print 'Bust! Uh-Oh'
                    self.busted = True
                    done = True
                if not done:
                    choice = raw_input('Your move: ')
            elif(choice == 'stay'):
                print 'Thank you'
                done = True
            else:
                print 'Not a valid move, try again.'
                choice = raw_input('Your move: ')
    
    def __str__(self):
        return '{player} bankroll: {bankroll}'.format(player=self.name,bankroll=self.bankroll)

class Game(object):

    def __init__(self,players=[Player(name='house')]):
        self.players = players

    def house_move(self,player,deck):
        """house hits until hand value >= 17"""
        limit = 17
        while player.hand.value() <= limit:
            player.hit(deck)
        return player.hand.value()

    def players_move(self,deck):
        #self.players[0] is the house, so iterate through self.players[1:]
        for player in self.players[1:]:
            player.move(deck)

    def meet_players(self):
        i = 0
        num_players = int(raw_input("How many players? "))
        #pdb.set_trace()
        while i < num_players:
            name = raw_input("Player {}, what's your name? "
                             .format(str(i+1))).lower()
            self.players.append(Player(name))
            i += 1

    def deal_cards(self,deck):
        #pdb.set_trace()
        for player in self.players:
            player.hand.deal(deck)

    def initial_bets(self):
        #remove first item in self.players because it is the house
        for player in self.players[1:]:
            player.hand.show()
            print "{}, the value of your hand is currently {}".format(player.name,player.hand.value())
            bet_val = int(raw_input("{}, make your bet: ".format(player.name)))
            player.bet = player.make_bet(bet_val)

    def payout(self):
        #self.players[0] is the house
        house = self.players[0]
        if not house.busted:
            for player in self.players[1:]:
                #player beats house
                if player.hand.value() > house.hand.value() and not player.busted:
                    player.bankroll += (player.bet*2)
                    print player
                #house beats player
                elif player.hand.value() < house.hand.value() or player.busted:
                    player.bankroll -= player.bet
                    print player
                #player gets blackjack
                elif player.hand.value() == 21:
                    player.bankroll += (player.bet*2.5)
                    print player
        else:
            for player in self.players[1:]:
                if not player.busted:
                    if player.hand.value() == 21:
                        player.bankroll += (player.bet)*2.5
                        print player
                    else:
                        player.backroll += (player.bet)*2
                        print player

    def cleanup_hands():
        for player in self.players[1:0]:
            player.hand = []

    def remove_players(self):
        player_done = raw_input('Would anyone like to leave the table? (y/n) ')
        while player_done == 'y':
            name = raw_input('Name: ').lower()
            for player in self.players:
                if player.name == name:
                    self.players.remove(player)
            player_done = raw_input('Anyone else? (y/n) ')

    def check_done(self):
        """returns 1 if game is over"""
        #if length of players list is 1, only the house if left
        if len(self.players) == 1:
            game_done = 0
        else:
            game_done = 1
        return game_done
