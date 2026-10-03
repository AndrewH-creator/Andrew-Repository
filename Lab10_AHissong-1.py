"""
Program Name: Word Count
Author: Andrew Hissong
Purpose: This program allows the user to select one of four predefined
         text files and analyzes the file by counting the frequency of
         every word. The results are displayed alphabetically.
Starter Code: None. Created for the Lab 10 assignment.
Date: October 3, 2026
"""

from pathlib import Path
import string


class WordAnalyzer:
    """Analyze a text file and count the frequency of each word."""

    def __init__(self, filepath):
        """Initialize the WordAnalyzer with a file path."""
        self.__filepath = Path(filepath)
        self.__frequencies = {}

    def process_file(self):
        """Read the file and count the frequency of each word."""
        try:
            if not self.__filepath.exists():
                raise FileNotFoundError

            translation_table = str.maketrans(
                "", "", string.punctuation
            )

            with self.__filepath.open("r", encoding="utf-8") as file:
                for line in file:
                    line = line.lower()
                    line = line.translate(translation_table)
                    words = line.split()

                    for word in words:
                        if word in self.__frequencies:
                            self.__frequencies[word] += 1
                        else:
                            self.__frequencies[word] = 1

            return True

        except FileNotFoundError:
            print(f"File not found: {self.__filepath}")
            return False

    def print_report(self):
        """Print the word frequency report alphabetically."""
        sorted_words = sorted(self.__frequencies.keys())

        for word in sorted_words:
            print(f"{word:<15} :: {self.__frequencies[word]}")


def main():
    """Run the Word Analyzer menu."""
    files = {
        "1": "princess_mars.txt",
        "2": "Tarzan.txt",
        "3": "treasure_island.txt",
        "4": "monte_cristo.txt"
    }

    file_names = {
        "1": "Princess of Mars",
        "2": "Tarzan",
        "3": "Treasure Island",
        "4": "Monte Cristo"
    }

    while True:
        print("\n--- Word Analyzer ---")
        print("Please select a file to analyze:")
        print("1. Princess of Mars")
        print("2. Tarzan")
        print("3. Treasure Island")
        print("4. Monte Cristo")
        print("5. Exit")


 choice = input("\nEnter your choice (1-5): ").strip()

        if choice == "5":
            print("\nGoodbye!")
            break

        if choice not in files:
            print("\nInvalid choice. Please select from 1-5.")
            input("\nPress Enter to return to the menu...")
            continue

        filepath = Path(files[choice])

        print(f"\nProcessing '{filepath.name}'...")
        print(f"Selected: {file_names[choice]}\n")

        analyzer = WordAnalyzer(filepath)

        if analyzer.process_file():
            analyzer.print_report()

        input("\nPress Enter to return to the menu...")
