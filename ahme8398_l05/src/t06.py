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
from functions import bag_to_set
# Constants

bag = input("Enter a list of values (separated by commas): ").split(',')
new_set = bag_to_set(bag)
new_set = list(map(int, new_set))
print("Final set:", new_set)