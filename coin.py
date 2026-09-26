"""
Program Name: Match Coins Game - Coin Class
Author: Andrew Hissong
Purpose: This file defines the Coin class used to represent a single
         tossable coin with a Heads or Tails state.
Starter Code: None
Date: September 26, 2026
"""

import random


class Coin:
    def __init__(self):
        self.__sideup = 'Heads'

    def toss(self):
        if random.randint(0, 1) == 0:
            self.__sideup = 'Heads'
        else:
            self.__sideup = 'Tails'

    def get_sideup(self):
        return self.__sideup
