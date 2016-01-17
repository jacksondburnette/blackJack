#!/usr/bin/env python
"""Classes to be used in blackJack game"""

class Player(object):

    def __init__(self,human=True,bankroll=0):
        self.human = human
        self.bankroll = bankroll

    def bankroll_add(amount):
        """Return players bankroll with amount added"""
        self.bankroll += amount
        return self.bankroll

    def bankroll_sub(amount):
        """Return players bankroll with amount subtracted"""
        self.bankroll -= amount
        return self.bankroll
