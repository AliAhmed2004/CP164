"""
-------------------------------------------------------
Array version of the List ADT.
-------------------------------------------------------
Author: Ali Ahmed
ID:     169038398
Email:  ahme8398@mylaurier.ca
__updated__ = "2023-03-04"
-------------------------------------------------------
"""
# pylint: disable=protected-access

# Imports
from copy import deepcopy


class List:

    def count_pairs(self):
        """
        -------------------------------------------------------
        Returns the number of pairs of values (identical values that are
        adjacent to each other) in source.
        Use: pairs = source.count_pairs(n)
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​‌​‌​​‌​​​‌‌‌‌‌​:
            pairs - the number of pairs in source (int >= 0)
        -------------------------------------------------------
        Examples:
            source: [3, 6, 5, 8, 6, 9]
                source.count_pairs() -> 0
            source: [3, 5, 5, 5, 8, 6, 6, 9]
                source.count_pairs() -> 3
        -------------------------------------------------------
        """

        # Your code here
        pairs = 0
        for i in range(len(self._values) - 1):
            if self._values[i] == self._values[i + 1]:
                pairs += 1
        return pairs

# DO NOT CHANGE CODE BELOW THIS LINE
# =======================================================================

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty list.
        Use: source = List()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​‌​‌​​‌​​​‌‌‌‌‌​:
            a new List object (List)
        -------------------------------------------------------
        """
        self._values = []

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if source is empty.
        Use: empty = source.is_empty()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​‌​‌​​‌​​​‌‌‌‌‌​:
            True if source is empty, False otherwise.
        -------------------------------------------------------
        """
        return len(self._values) == 0

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the number of values in source.
        Use: n = len(source)
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​‌​‌​​‌​​​‌‌‌‌‌​:
            the number of values in source.
        -------------------------------------------------------
        """
        return len(self._values)

    def prepend(self, value):
        """
        -------------------------------------------------------
        Adds a copy of value to the front of source.
        Use: source.prepend(value)
        -------------------------------------------------------
        Parameters:
            value - a data element. (*)
        Returns‌​‌​​​​‌​​‌‌​‌​‌​​‌​​​‌‌‌‌‌​:
            None
        -------------------------------------------------------
        """
        self._values[:] = [deepcopy(value)] + self._values
        return

    def append(self, value):
        """
        ---------------------------------------------------------
        Adds a copy of value to the end of source.
        Use: source.append(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (*)
        Returns‌​‌​​​​‌​​‌‌​‌​‌​​‌​​​‌‌‌‌‌​:
            None
        -------------------------------------------------------
        """
        self._values = self._values + [deepcopy(value)]
        return

    def insert(self, i, value):
        """
        -------------------------------------------------------
        A copy of value is added to source at index i, following values are
        pushed right.
        If i outside of range of -len(list) to len(list) - 1, value is
        prepended or appended as appropriate.
        Use: source.insert(i, value)
        -------------------------------------------------------
        Parameters:
            i - index value (int)
            value - a data element (*)
        Returns‌​‌​​​​‌​​‌‌​‌​‌​​‌​​​‌‌‌‌‌​:
            None
        -------------------------------------------------------
        """
        self._values[:] = self._values[:i] + \
            [deepcopy(value)] + self._values[i:]
        return

    def _linear_search(self, key):
        """
        -------------------------------------------------------
        Searches for the first occurrence of key in self.
        Private helper method.
        Use: i = self._linear_search(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (*)
        Returns‌​‌​​​​‌​​‌‌​‌​‌​​‌​​​‌‌‌‌‌​:
            i - the index of key in self, -1 if key is not found (int)
        -------------------------------------------------------
        """
        n = len(self._values)
        i = 0

        while i < n and self._values[i] != key:
            i += 1

        if i == n:
            i = -1
        return i

    def remove(self, key):
        """
        -------------------------------------------------------
        Finds, removes, and returns the first value in source that matches key.
        Use: value = source.remove(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (*)
        Returns‌​‌​​​​‌​​‌‌​‌​‌​​‌​​​‌‌‌‌‌​:
            value - the full value matching key, otherwise None (*)
        -------------------------------------------------------
        """
        # Key argument exists - search list for key.
        i = self._linear_search(key)

        if i > -1:
            value = self._values.pop(i)
        else:
            value = None
        return value

    def find(self, key):
        """
        -------------------------------------------------------
        Finds and returns a copy of the first value in source that matches key.
        Use: value = source.find(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (*)
        Returns‌​‌​​​​‌​​‌‌​‌​‌​​‌​​​‌‌‌‌‌​:
            value - a copy of the full value matching key, otherwise None (*)
        -------------------------------------------------------
        """
        i = self._linear_search(key)

        if i > -1:
            value = deepcopy(self._values[i])
        else:
            value = None
        return value

    def peek(self):
        """
        -------------------------------------------------------
        Returns a copy of the first value in source.
        Use: value = source.peek()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​‌​‌​​‌​​​‌‌‌‌‌​:
            value - a copy of the first value in source (*)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot peek at an empty list"

        value = deepcopy(self._values[0])
        return value

    def index(self, key):
        """
        -------------------------------------------------------
        Finds the index of the location of key in source.
        Use: n = source.index(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (*)
        Returns‌​‌​​​​‌​​‌‌​‌​‌​​‌​​​‌‌‌‌‌​:
            i - the index of the location of key in source, -1 if
              key is not in source. (int)
        -------------------------------------------------------
        """
        i = self._linear_search(key)
        return i

    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Determines if source contains key.
        Use: b = key in source
        -------------------------------------------------------
        Parameters:
            key - a partial data element (*)
        Returns‌​‌​​​​‌​​‌‌​‌​‌​​‌​​​‌‌‌‌‌​:
            True if source contains key, False otherwise. (boolean)
        -------------------------------------------------------
        """
        i = self._linear_search(key)
        return i > -1

    def pop(self, *args):
        """
        -------------------------------------------------------
        Finds, removes, and returns the value in source whose index matches i.
        Use: value = source.pop()
        Use: value = source.pop(i)
        -------------------------------------------------------
        Parameters:
            args - an array of arguments (tuple of int)
            args[0], if it exists, is the index i
        Returns‌​‌​​​​‌​​‌‌​‌​‌​​‌​​​‌‌‌‌‌​:
            value - if args exists, the value at position args[0],
                otherwise the last value in source, value is
                removed from source (*)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot pop from an empty list"
        assert len(args) <= 1, "No more than 1 argument allowed"

        if len(args) == 1:
            # pop the element at position i
            i = args[0]
            value = self._values.pop(i)
        else:
            # pop the last element
            value = self._values.pop()
        return value

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through source
        from front to rear.
        Use: for v in source:
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​‌​‌​​‌​​​‌‌‌‌‌​:
            value - the next value in source (*)
        -------------------------------------------------------
        """
        for value in self._values:
            yield value
