"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ali Ahmed
ID:      169038398
Email:   ahme8398@mylaurier.ca
__updated__ = "2023-02-11"
-------------------------------------------------------
"""
# Imports
from Queue_array import Queue
# Constants

source1 = Queue()
source2 = Queue()
target = Queue()

num1 = int(input("Enter the number of elements for source1: "))
for i in range(num1):
    value = int(input("Enter a value for source1: "))
    source1.insert(value)

print(" ")

num2 = int(input("Enter the number of elements for source2: "))
for i in range(num2):
    value = int(input("Enter a value for source2: "))
    source2.insert(value)

target.combine(source1, source2)

print(" ")

print("Target:")
while not target.is_empty():
    print(target.remove(), end=" ")
