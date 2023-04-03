"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ali Ahmed
ID:      169038398
Email:   ahme8398@mylaurier.ca
__updated__ = "2023-01-27"
-------------------------------------------------------
"""
# Imports
from utilities import stack_to_array
from Stack_array import Stack
# Constants

target = [int(i) for i in input(
    "Enter a list of values separated by commas: ").split(",")]

stack = Stack()

stack_to_array(stack, target)
stack = list(map(int, stack))
print("Stack: ", stack)
print("Target: ", target)
