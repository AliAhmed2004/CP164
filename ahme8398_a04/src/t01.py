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
from Queue_circular import Queue
# Constants


source = Queue()

num_values = int(
    input("How many values do you want to insert into the queue? "))

print("\nEnter the values:")
for i in range(num_values):
    value = int(input(f"Enter value {i + 1}: "))
    source.insert(value)

print("\nValues in the queue:")
for i in source:
    print(i)

print()

empty = source.is_empty()
full = source.is_full()
source_len = len(source)

if not empty:
    remove = source.remove()
    print(f"Removed value: {remove}")
else:
    print("Queue is empty, cannot remove an item.")

peek = source.peek()

print(f"Is source empty?: {empty}")
print()
print(f"Is source full?: {full}")
print()
print(f"Length of source: {source_len}")
