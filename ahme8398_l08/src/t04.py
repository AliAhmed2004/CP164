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
from morse import ByCode, fill_code_bst
from BST_linked import BST
# Constants

a = ByCode('A', '.-')
b = ByCode('B', '-...')
c = ByCode('C', '-.-.')

bst = BST()

values = [(a.letter, a.code), (b.letter, b.code), (c.letter, c.code)]
fill_code_bst(bst, values)

v = bst.inorder()

for i in v:
    print(i)