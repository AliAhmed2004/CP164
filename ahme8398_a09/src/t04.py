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
from BST_linked import BST
# Constants

arr = [2,43,65,112,66,26,98,67,87]

bst = BST()

for val in arr:
    bst.insert(val)
    
print("BST: ")
for i in bst:
    print(i)
    
print(" ")
print("--node_counts--")
zero, one, two = bst.node_counts()
print(f"Zero: {zero}")
print(f"One: {one}")
print(f"Two: {two}")

print(" ")
print("--__contains__--")
b = 65
print(f"Does BST contain {b}?")
print(b in bst)

print(" ")
print("--parent--")
print(f"Parent of 87: {bst.parent(87)}")

print(" ")
print("--parent_r--")
print(f"Parent of 98: {bst.parent_r(98)}")