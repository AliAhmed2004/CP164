"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ali Ahmed
ID:      169038398
Email:   ahme8398@mylaurier.ca
__updated__ = "2023-02-02"
-------------------------------------------------------
"""
# Imports
from functions import is_mirror_stack
# Constants     

string = input("Enter the string: ")
valid_chars = input("Enter the valid characters: ")
m = input("Enter the mirror pivot character: ")

mirror = is_mirror_stack(string, valid_chars, m)
print(f"Mirror: {mirror.value}")