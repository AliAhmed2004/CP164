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
from List_linked import List
# Constants

lst = List()

values = input("Enter values for list seperated by spaces: ").split()

for i in values:
    lst.append(int(i))

print("List elements:", end=" ")
for value in lst:
    print(value, end=" ")
    
lst.reverse_r()

print()
print("Reversed list elements:", end=" ")
for value in lst:
    print(value, end=" ")