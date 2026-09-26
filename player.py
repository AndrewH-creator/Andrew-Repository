"""
Program Name: Match Coins Game - Player Class
Author: Andrew Hissong
Purpose: This file defines the Player class. A Player has a name,
         a wallet of coins, and a Coin object to toss.
Starter Code: None
Date: September 26, 2026
"""


from coin import Coin


class Player:
    def __init__(self, name):
        self.__name = name
        self.__wallet = 20
        self.__coin = Coin()

    def toss_coin(self):
        self.__coin.toss()

    def get_coin_side(self):
        return self.__coin.get_sideup()

    def win_coin(self):
        self.__wallet += 1

    def lose_coin(self):
        self.__wallet -= 1

    def get_wallet(self):
        return self.__wallet

    def get_name(self):
        return self.__name
