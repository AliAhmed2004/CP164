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

lst1 = List()

values1 = input("Enter values for list 1 seperated by spaces: ").split()

for i in values1:
    lst1.append(int(i))

print("List 1 elements:", end=" ")
for value in lst1:
    print(value, end=" ")
    
print()

lst2 = List()

values2 = input("Enter values for list 2 seperated by spaces: ").split()

for i in values2:
    lst2.append(int(i))

print("List 2 elements:", end=" ")
for value in lst2:
    print(value, end=" ")
    
print()

lst3 = List()
lst3.union_r(lst1, lst2)

print("List 3 elements --union--:", end=" ")
for value in lst3:
    print(value, end=" ")