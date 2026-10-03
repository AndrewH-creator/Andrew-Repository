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
