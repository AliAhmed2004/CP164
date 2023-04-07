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
from Sorts_Deque_linked import Sorts
from Deque_linked import Deque
# Constants

d = Deque()

arr = [12,43,65,98,57,4,8,25,33,41]

for val in arr:
    d.insert_front(val)

print ("Original Deque:")
for i in d:
    print (i)

Sorts.gnome_sort(d)

print ("\nAfter Gnome Sort:")
for i in d:
    print (i)