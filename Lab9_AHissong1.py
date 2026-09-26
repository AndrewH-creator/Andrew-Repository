"""
Program Name: Match Coins Game
Author: Andrew Hissong
Purpose: This program runs a two-player coin matching game.
         Players toss coins and gain or lose coins based on
         whether the two coin sides match.
Starter Code: None
Date: September 26, 2026
"""

from player import Player


def main():
    player1 = Player("Player 1")
    player2 = Player("Player 2")

    print("--- Coin Match Game ---")
    print(f"{player1.get_name()} has {player1.get_wallet()} coins.")
    print(f"{player2.get_name()} has {player2.get_wallet()} coins.")

    play_again = input("\nDo you want to toss the coins? (y/n): ")
