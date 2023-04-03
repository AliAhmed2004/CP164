"""
-------------------------------------------------------
Array version of the Queue ADT.
-------------------------------------------------------
Author: Ali Ahmed
ID:     169038398
Email:  ahme8398@mylaurier.ca
__updated__ = "2023-03-04"
-------------------------------------------------------
"""
# pylint: disable=protected-access

from copy import deepcopy


class Queue:

    def rotate(self, n):
        """
        -------------------------------------------------------
        Rotates position of values in source. When finished values
        in source are rotated n positions to the right.
        Use: source.rotate(n)
        -------------------------------------------------------
        Parameters:
            n - amount to rotate Queue values (int)
        Returns‌​‌​​​​‌​​‌‌​‌​‌​​‌​​​‌‌‌‌‌​:
            None
        -------------------------------------------------------
        Examples:

        -------------------------------------------------------
        """

        # your code here

        return

# DO NOT CHANGE CODE BELOW THIS LINE
# =======================================================================

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty Queue. Data is stored in a Python list.
        Use: source = Queue()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​‌​‌​​‌​​​‌‌‌‌‌​:
            a new Queue object (Queue)
        -------------------------------------------------------
        """
        self._values = []

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if source is empty.
        Use: b = source.is_empty()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​‌​‌​​‌​​​‌‌‌‌‌​:
            True if source is empty, False otherwise.
        -------------------------------------------------------
        """
        return len(self._values) == 0

    def is_full(self):
        """
        -------------------------------------------------------
        Determines if source is full. (Given the expandable nature
        of the Python list _values, source is never full.)
        Use: b = source.is_full()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​‌​‌​​‌​​​‌‌‌‌‌​:
            True if source is full, False otherwise.
        -------------------------------------------------------
        """
        return False

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the length of source.
        Use: n = len(source)
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​‌​‌​​‌​​​‌‌‌‌‌​:
            the number of values in source.
        -------------------------------------------------------
        """
        return len(self._values)

    def insert(self, value):
        """
        -------------------------------------------------------
        Adds a copy of value to the rear of source.
        Use: source.insert(value)
        -------------------------------------------------------
        Parameters:
            value - data (*)
        Returns‌​‌​​​​‌​​‌‌​‌​‌​​‌​​​‌‌‌‌‌​:
            None
        -------------------------------------------------------
        """
        self._values.append(deepcopy(value))
        return

    def remove(self):
        """
        -------------------------------------------------------
        Removes and returns the front value from source.
        Use: value = source.remove()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​‌​‌​​‌​​​‌‌‌‌‌​:
            value - the value at the front of source - the value is
            removed from source (*)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot remove from an empty queue"

        value = self._values.pop(0)
        return value

    def peek(self):
        """
        -------------------------------------------------------
        Peeks at the front of source.
        Use: value = source.peek()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​‌​‌​​‌​​​‌‌‌‌‌​:
            value - a copy of the value at the front of source -
            the value is not removed from source (*)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot peek at an empty queue"

        value = deepcopy(self._values[0])
        return value

    def __eq__(self, target):
        """
        ----------------
        Determines whether source and target are equivalent.
        Values in source and target are compared and if all values are equal
        and in the same order, returns True, otherwise returns False.
        Use: equals = source == target
        ---------------
        Parameters:
            target - a queue (Queue)
        Returns‌​‌​​​​‌​​‌‌​‌​‌​​‌​​​‌‌‌‌‌​:
            equals - True if source contains the same values
                as target in the same order, otherwise False. (boolean)
        ---------------
        """
        equals = False

        if len(self._values) == len(target._values):
            i = 0

            while i < len(self._values) and self._values[i] == target._values[i]:
                # Compare each element, stop when the elements are not the same
                # or the end of the Queues are reached.
                i += 1
            equals = i == len(self._values)
        return equals

    def __iter__(self):
        """
        FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through source
        from front to rear.
        Use: for value in source:
        -------------------------------------------------------
        Yields:
            value - the next value in source (*)
        -------------------------------------------------------
        """
        for value in self._values:
            yield value
