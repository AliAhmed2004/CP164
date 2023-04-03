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
from functions import to_power
# Constants

base = float(input("Enter the base: "))
power = int(input("Enter the power: "))

ans = to_power(base, power)

print("Result:", ans)