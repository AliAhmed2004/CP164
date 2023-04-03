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
from functions import postfix
# Constants 

expression = input("Enter a postfix expression: ")
result = postfix(expression)
print("Answer = ", result)