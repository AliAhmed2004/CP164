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
from test_Sorts_List_linked import create_randoms, create_reversed, create_sorted
# Constants

sorted_list = create_sorted()
reversed_list = create_reversed()
random_list = create_randoms()

print("Sorted:")
for num in sorted_list:
    print(num)

print("Reversed:")
for num in reversed_list:
    print(num)

print("Random Lists:")
print("[", end="")
for i in random_list:
    print("[", end="")
    for k in i:
        print(k, end=", ")
    print("]", end="")