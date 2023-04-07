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
from Sorts_array import Sorts
# Constants

print("Array before gnome sort: ")
arr = [12,43,65,98,57,4,8,25,33,41]
print(arr)
Sorts.gnome_sort(arr)
print("\nArray after gnome sort: ")
print(arr)