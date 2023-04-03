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
from Stack_array import Stack
from functions import stack_split_alt
# Constants

source = Stack()
while True:
    user_input = input("Enter a value to add to the source stack (enter 'x' to quit): ")
    if user_input == 'x':
        break
    else:
        source.push(user_input)

target1, target2 = stack_split_alt(source)
print("Target stack 1:")
while not target1.is_empty():
    print(target1.pop())

print("Target stack 2:")
while not target2.is_empty():
    print(target2.pop())

