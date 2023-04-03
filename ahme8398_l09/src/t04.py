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

hset = Hash_Set(5)
for i in range(8):
    hset.insert(i)

print("Before rehashing:")
hset.debug()

hset._rehash()

print("\nAfter rehashing:")
hset.debug()