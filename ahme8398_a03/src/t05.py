"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Ali Ahmed
ID:      169038398
Email:   ahme8398@mylaurier.ca
__updated__ = "2023-02-02"
-------------------------------------------------------
"""
# Imports
from functions import stack_maze
# Constants     
"""
print("Enter the maze details in the following format => Name: [branch1, branch2, ... branchn].")
print("Enter 'X' for the exit point and 'End' when done.")
maze = {}
while True:
    user_input = input().split(': ')
    if user_input[0] == 'End':
        break
    maze[user_input[0]] = list(map(str, user_input[1][1:-1].split(', ')))
path = stack_maze(maze)

print(" ")

if path:
    print("The exit route is:")
    print(path)
else:
    print("The exit route is:")
    print(path)
    """

maze = {'Start': ['A'], 'A':['B', 'C'], 'B':[], 'C':['D', 'E'],
    'D':[], 'E': ['X', 'F'], 'F':['G'], 'G':['C']}

print(stack_maze(maze))