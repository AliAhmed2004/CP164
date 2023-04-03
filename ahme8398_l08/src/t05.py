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
from morse import ByLetter, encode_morse, fill_letter_bst
from BST_linked import BST
# Constants

a = ByLetter('A', '.-')
b = ByLetter('B', '-...')
c = ByLetter('C', '-.-.')

bst = BST()
values = [(a.letter, a.code), (b.letter, b.code), (c.letter, c.code)]
fill_letter_bst(bst, values)
bst.inorder()
text = "ABC"
result = encode_morse(bst, text)

print(result)