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
from functions import gcd
# Constants

m = int(input("Enter an integer: "))
n = int(input("Enter another integer: "))

ans = gcd(m, n)

print("The GCD of", m, "and", n, "is:", ans)