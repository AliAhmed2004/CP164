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
from Hash_Set_array import Hash_Set
# Constants

print("Testing insert:")
hset = Hash_Set(1)
hset.insert(2)
hset.insert(3)
hset.insert(4)
hset.insert(5)

print("Hash set after inserting: ")
for i in hset:
    print(i)
    
print(" ")

print("Testing remove:")

removed = hset.remove(3)

print("Removed value: ", removed)

print("Hash set after removing: ")
for i in hset:
    print(i)