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
from morse import ByLetter, fill_letter_bst
from BST_linked import BST
# Constants

a = ByLetter('A', '.-')
b = ByLetter('B', '-...')
c = ByLetter('C', '-.-.')

bst = BST()

values = [(a.letter, a.code), (b.letter, b.code), (c.letter, c.code)]
fill_letter_bst(bst, values)

v = bst.inorder()

for i in v:
    print(i)