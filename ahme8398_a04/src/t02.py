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
target = Queue()

num_values = int(input(
    "How many values do you want to insert into the queue for source and target?: "))

for i in range(num_values):
    source_value = int(input(f"Enter value for source queue {i + 1}: "))
    source.insert(source_value)

    target_value = int(input(f"Enter value for target queue {i + 1}: "))
    target.insert(target_value)

equals = source == target

print(f"Is source and target equal?: {equals}")
