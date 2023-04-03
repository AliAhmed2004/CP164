"""
-------------------------------------------------------
Array version of the Sorted_Set ADT.
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


class Sorted_Set:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty set.
        Use: source = Sorted_Set()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​‌​‌​​‌​​​‌‌‌‌‌​:
            a new Sorted_Set object. (Sorted_Set)
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

        # Your code here
        empty = False
        if len(self._values) == 0:
            empty = True

        return empty

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the number of values in source.
        Use: n = len(source)
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​‌​‌​​‌​​​‌‌‌‌‌​:
            the number of values in source. (int)
        -------------------------------------------------------
        """

        # Your code here

        return len(self._values)

    def _binary_search(self, key):
        """
        -------------------------------------------------------
        Searches for the first occurrence of key in self.
        (Private helper method - used only by other ADT methods.)
        Use: i = self._binary_search(key)
        -------------------------------------------------------
        Parameters:
            key - a data value (*)
        Returns‌​‌​​​​‌​​‌‌​‌​‌​​‌​​​‌‌‌‌‌​:
            i - the index of the only occurrence of key in
                self, -1 if key is not found. (int)
        -------------------------------------------------------
        """

        # Your code here
        low = 0
        high = len(self._values) - 1
        while low < high:
            mid = (high - low) // 2 + low
            if key > self._values[mid]:
                low = mid + 1
            else:
                high = mid
        if low == high and self._values[low] == key:
            i = low
        else:
            i = -1
        return i

    def add(self, value):
        """
        -------------------------------------------------------
        If value does not already exist in source, adds a copy of value
        to source. Returns True if value is added, False otherwise.
        Values in source must remain sorted.
        Use: added = source.add(value)
        -------------------------------------------------------
        Parameters:
            value - data (*)
        Returns‌​‌​​​​‌​​‌‌​‌​‌​​‌​​​‌‌‌‌‌​:
            added - True if value added to source, False otherwise. (bool)
        -------------------------------------------------------
        """
        added = False
        if value in self._values:
            added = False
        else:
            index = 0
            while index < len(self._values) and value > self._values[index]:
                index += 1
            self._values.insert(index, value)
            added = True
        
        return added


    def discard(self, key):
        """
        -------------------------------------------------------
        Finds, removes, and returns the value in source that matches key.
        Returns None if key not in source.
        Use: value = source.discard(key)
        -------------------------------------------------------
        Parameters:
            key - data key (*)
        Returns‌​‌​​​​‌​​‌‌​‌​‌​​‌​​​‌‌‌‌‌​:
            value - the full value matching key, None otherwise. (*)
        -------------------------------------------------------
        """
        value = None
        i = 0
        while i < len(self._values):
            if self._values[i] == key:
                value = self._values.pop(i)
                break
            i += 1
        return value

    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Returns True if source contains key, False otherwise.
        Use: b = key in source
        -------------------------------------------------------
        Parameters:
            key - data key. (*)
        Returns‌​‌​​​​‌​​‌‌​‌​‌​​‌​​​‌‌‌‌‌​:
            True if source contains key, False otherwise. (bool)
        -------------------------------------------------------
        """
        contains = False
        for value in self._values:
            if value == key:
                contains = True
        return contains

    def __eq__(self, target):
        """
        ---------------------------------------------------------
        Determines whether source == target are equivalent.
        Values in source and target are compared and if all values are equal
        and in the same order, returns True, otherwise returns False.
        Use: source == target
        -------------------------------------------------------
        Parameters:
            target - Sorted_Set to compare against (Sorted_Set)
        Returns‌​‌​​​​‌​​‌‌​‌​‌​​‌​​​‌‌‌‌‌​:
            equals - True if source contains the same values as target,
                False otherwise. (bool)
        -------------------------------------------------------
        Examples:
            {1,2,3} == {1,2,3}: True
            {1,2,3} == {1,2,4}: False
            {1,2,3} == {1,2,3,4}: False
        -------------------------------------------------------
        """
        if self is target:
            result = True
        elif len(self) != len(target):
            result = False
        elif self.is_empty() and target.is_empty():
            result = True
        elif self._values[0] != target._values[0]:
            result = False
        else:
            i = 0
            j = 0
            while i < len(self) and j < len(target):
                if self._values[i] == target._values[j]:
                    i += 1
                    j += 1
                elif self._values[i] < target._values[j]:
                    result = False
                    break
                else:
                    j += 1
            else:
                result = True

        return result

    def issubset(self, target):
        """
        ---------------------------------------------------------
        Tests whether every value in source is also in target.
        Use: subset = source.issubset(target)
        -------------------------------------------------------
        Parameters:
            target - another Sorted_Set. (Sorted_Set)
        Returns‌​‌​​​​‌​​‌‌​‌​‌​​‌​​​‌‌‌‌‌​:
            subset - True if all values in source are also in target,
                False otherwise. (bool)
        -------------------------------------------------------
        Examples:
            {1,2,3}.issubset({0,1,2,3,4}): True
            {1,2,3}.issubset({1,2,4,5}): False
        -------------------------------------------------------
        """
        subset = True
        if len(self) > len(target):
            subset = False
        
        for value in self:
            if value not in target:
                subset = False
            
        return subset

    def isdisjoint(self, target):
        """
        -------------------------------------------------------
        Return True if source has no values in common with target.
        Sorted_Sets are disjoint if and only if their intersection
        is the empty Sorted_Set.
        Use: disjoint = source.isdisjoint(target)
        -------------------------------------------------------
        Parameters:
            target - a Sorted_Set to compare against source. (Sorted_Set)
        Returns‌​‌​​​​‌​​‌‌​‌​‌​​‌​​​‌‌‌‌‌​:
            disjoint - True if source has no values in common with target,
                False otherwise. (bool)
        -------------------------------------------------------
        Examples:
            {1,2,3}.isdisjoint({4,5,6,7}): True
            {1,2,3}.isdisjoint({1,4,5,6,7}): False
        -------------------------------------------------------
        """
        disjount = True
        for value in self:
            if value in target:
                disjount = False
        
        return disjount

    def intersection(self, source2):
        """
        -------------------------------------------------------
        Return target with copies of values common to source1 and source2.
        Values may appear only once in target. Values must be sorted.
        Use: target = source1.intersection(source2)
        -------------------------------------------------------
        Parameters:
            source2 - an array-based Sorted_Set. (Sorted_Set)
        Returns‌​‌​​​​‌​​‌‌​‌​‌​​‌​​​‌‌‌‌‌​:
            target - the intersection of source1 and source2. (Sorted_Set)
        -------------------------------------------------------
        Examples:
            {1,2,3}.intersection({3,4,5}): {3}
            {1,2,3}.intersection({4,5,6}): {}
        -------------------------------------------------------
        """
        target = Sorted_Set()

        for value in self._values:
            if source2._binary_search(value) != -1 and target._binary_search(value) == -1:
                target._values.append(value)

        return target

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through source
        from front to rear.
        Use: for v in source:
        -------------------------------------------------------
        Returns‌​‌​​​​‌​​‌‌​‌​‌​​‌​​​‌‌‌‌‌​:
            value - the next value in the Sorted_Set. (*)
        -------------------------------------------------------
        """
        for value in self._values:
            yield value
