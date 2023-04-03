"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ali Ahmed
ID:      169038398
Email:   ahme8398@mylaurier.ca
__updated__ = "2023-02-07"
-------------------------------------------------------
"""
# Imports
from List_array import List
from utilities import array_to_list, list_to_array
# Constants

# Array to list
llist = List()
print("Testing for array to list")
source = list(map(int, input("Enter elements for source list (seperated by commas): ").split(',')))

array_to_list(llist, source)

values = []
for value in llist:
    values.append(value)

print("Array to list:", values)

print("")

# List to array
llist = List()
print("Testing for list to array")
source = list(map(int, input("Enter elements for source list (separated by commas): ").split(',')))
target = list(map(int, input("Enter elements for target list (separated by commas): ").split(',')))

list_to_array(llist, target)

print("Target list:", target)