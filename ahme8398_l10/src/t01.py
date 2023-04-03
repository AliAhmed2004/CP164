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
from test_Sorts_array import create_randoms, create_reversed, create_sorted
# Constants

sorted_array = create_sorted()
reversed_array = create_reversed()
random_arrays = create_randoms()

print("Sorted:")
for num in sorted_array:
    print(num)

print("Reversed:")
for num in reversed_array:
    print(num)

print("Random Lists:")
print("[", end="")
for i in random_arrays:
    print("[", end="")
    for k in i:
        print(k, end=", ")
    print("]", end="")