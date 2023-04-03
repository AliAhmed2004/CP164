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
from functions import queue_combine
# Constants

print("Enter values for first queue (separated by commas):")
source1_values = input().strip().split(', ')
source1 = Queue()
for value in source1_values:
    source1.insert(int(value))

print("Enter values for second queue (separated by commas):")
source2_values = input().strip().split(', ')
source2 = Queue()
for value in source2_values:
    source2.insert(int(value))

target = queue_combine(source1, source2)

print("Values in target queue:")
while not target.is_empty():
    value = target.remove()
    if target.is_empty():
        print(value)
    else:
        print(value, end=", ")
