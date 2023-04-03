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
from Priority_Queue_array import Priority_Queue
# Constants

pq = Priority_Queue()

n = int(input("How many values do you want to insert into the source priority queue?: "))

for i in range(n):
    value = int(input(f"Enter value for source priority queue {i + 1}: "))
    pq.insert(value)

key = int(input("Enter the key to split the source priority queue: "))

target1, target2 = pq.split_key(key)

print("\nValues in target1:")
for i in target1:
    print(i)

print("\nValues in target2:")
for i in target2:
    print(i)
