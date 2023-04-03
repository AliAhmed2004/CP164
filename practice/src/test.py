"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ali Ahmed
ID:      169038398
Email:   ahme8398@mylaurier.ca
__updated__ = "2023-01-09"
-------------------------------------------------------
"""
# Imports
# Constants


class Number:
    def __init__(self, value):
        self.value = value
        return

    def square(self):
        result = self.value * self.value
        return result


example = Number(5)
answer = example.square()
print(answer)
