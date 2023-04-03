"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ali Ahmed
ID:      169038398
Email:   ahme8398@mylaurier.ca
__updated__ = "2023-02-09"
-------------------------------------------------------
"""
# Imports
from functions import is_palindrome
# Constants

s = input("Enter a string: ")

palindrome = is_palindrome(s)

print("Palindrome: {}".format(palindrome))