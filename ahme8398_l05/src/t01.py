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
from functions import recurse
# Constants

x = int(input("Enter an integer: "))
y = int(input("Enter another integer: "))

ans = recurse(x, y)

print("Final result:", ans)


