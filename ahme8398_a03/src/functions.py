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
from ahme8398_data_structures.src.Stack_array import Stack
from enum import Enum
# Constants
OPERATORS = "+-*/"

# Enumerated constant
MIRRORED = Enum('MIRRORED',
                {'IS_MIRRORED': "is a mirror", 'TOO_MANY_LEFT': "too many characters in L",
                 'TOO_MANY_RIGHT': "too many characters in R", 'MISMATCHED': "L and R don't match",
                 'INVALID_CHAR': "invalid character", 'NOT_MIRRORED': "no mirror character"})


def stack_split_alt(source):
    """
    -------------------------------------------------------
    Splits the source stack into separate target stacks.
    When finished source stack is empty. Values are
    pushed alternately onto the returned target stacks.
    Use: target1, target2 = stack_split_alt(source)
    -------------------------------------------------------
    Parameters:
        source - the stack to split into two parts (Stack)
    Returns:
        target1 - contains alternating values from source (Stack)
        target2 - contains other alternating values from source (Stack)
    -------------------------------------------------------
    """
    stack1 = Stack()
    stack2 = Stack()

    while not source.is_empty():
        stack1.push(source.pop())

        if not source.is_empty():
            stack2.push(source.pop())

    target1 = Stack()
    target2 = Stack()
    while not stack1.is_empty():
        target1.push(stack1.pop())
    while not stack2.is_empty():
        target2.push(stack2.pop())

    return target1, target2

def is_palindrome_stack(string):
    """
    -------------------------------------------------------
    Determines if string is a palindrome. Ignores case, digits, spaces, and
    punctuation in string.
    Use: palindrome = is_palindrome_stack(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        palindrome - True if string is a palindrome, False otherwise (bool)
    -------------------------------------------------------
    """
    stack = Stack()
    string = string.lower()
    string = ''.join(filter(str.isalnum, string)) # removes all non-alphanumeric characters
    palindrome = True

    # Pushes all characters in string onto stack
    for char in string:
        stack.push(char)
    
    # Pops all characters from stack and compares them to the first character in string
    while not stack.is_empty():
        if stack.pop() != string[0]:
            palindrome = False
        string = string[1:]
    
    return palindrome

def postfix(string):
    """
    -------------------------------------------------------
    Evaluates a postfix expression.
    Use: answer = postfix(string)
    -------------------------------------------------------
    Parameters:
        string - the postfix string to evaluate (str)
    Returns:
        answer - the result of evaluating string (float)
    -------------------------------------------------------
    """
    stack = Stack()
    
    for char in string.split():
        if char.isdigit():
            stack.push(int(char))
        elif char in OPERATORS:
            sign2 = stack.pop()
            sign1 = stack.pop()
            if char == '+':
                result = sign1 + sign2
            elif char == '-':
                result = sign1 - sign2
            elif char == '*':
                result = sign1 * sign2
            else:
                result = sign1 / sign2
            stack.push(result)
    answer = stack.pop()
    
    return answer

def stack_maze(maze):
    """
    -------------------------------------------------------
    Solves a maze using Depth-First search.
    Use: path = stack_maze(maze)
    -------------------------------------------------------
    Parameters:
        maze - dictionary of points in a maze, where each point
            represents a corridor end or a branch. Dictionary
            keys are the name of the point followed by a list of
            branches, if any. First point is named 'Start', exit
            is named 'X' (dict)
    Returns:
        path - list of points visited before the exit is reached,
            None if there is no exit (list of str)
    -------------------------------------------------------
    """
    stack = Stack()
    path = []
    last_position = {}
    start = 'Start'
    
    stack.push(start)
    last_position[start] = []

    while not stack.is_empty():
        current_position = stack.pop()
        path.append(current_position)
        if current_position == 'X':
            path.pop(0)
            return path
        for node in maze.get(current_position, []):
            if node not in last_position:
                stack.push(node)
                last_position[node] = path
                
def is_mirror_stack(string, valid_chars, m):
    """
    -------------------------------------------------------
    Determines if string is a mirror of characters in valid_chars around the pivot m.
    A mirror is of the form LmR, where L is the reverse of R, and L and R
    contain only characters in valid_chars.
    Use: mirror = is_mirror_stack(string, valid_chars, m)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
        valid_chars - a string of valid characters (str)
        m - the mirror pivot string (str - one character not in valid_chars)
    Returns:
        mirror - the state of the string (Enum MIRRORED)
    -------------------------------------------------------
    """
    assert m not in valid_chars, \
        f"cannot use '{m}' as the mirror character"

    stack = Stack()
    mirror = MIRRORED.IS_MIRRORED
    
    i = 0
    left_count = 0
    while i < len(string) and string[i] != m:
        if string[i] not in valid_chars:
            mirror = MIRRORED.INVALID_CHAR
        stack.push(string[i])
        left_count += 1
        i += 1
    if i == len(string):
        mirror = MIRRORED.NOT_MIRRORED
    i += 1
    right_count = 0
    while i < len(string):
        if string[i] not in valid_chars:
            mirror = MIRRORED.INVALID_CHAR
        if stack.is_empty():
            mirror = MIRRORED.TOO_MANY_RIGHT
        if stack.pop() != string[i]:
            mirror = MIRRORED.MISMATCHED
        right_count += 1
        i += 1
    if not stack.is_empty():
        mirror = MIRRORED.TOO_MANY_LEFT
    if left_count > right_count:
        mirror = MIRRORED.NOT_MIRRORED
    
    return mirror