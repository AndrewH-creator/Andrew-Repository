"""
Program Name: Lab 1 - UPC Validator
Author: Andrew Hissong
Purpose: This program validates a 12-digit UPC-A code by calculating
         the expected check digit and comparing it to the check digit
         provided by the user.
Starter Code: None. This program was written from the assignment requirements.
Date: September 17, 2026
"""
def find_UPC(upc_first_11):
    """
    Calculates and returns the expected UPC-A check digit.
    """

    total = 0

    for i in range(11):
        digit = int(upc_first_11[i])

        if i % 2 == 0:
            total += digit * 3
        else:
            total += digit

    check_digit = (10 - (total % 10)) % 10

    return check_digit
def main():
    """Gets a UPC from the user and determines whether it is valid."""

    while True:
        upc = input("Enter a 12-digit UPC: ")

        if len(upc) == 12 and upc.isdigit():
            break

        print("Error: Please enter exactly 12 digits.")
