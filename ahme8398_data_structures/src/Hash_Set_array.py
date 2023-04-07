"""
-------------------------------------------------------
Array-based list version of the Hash Set ADT.
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2023-04-02"
-------------------------------------------------------
"""
# pylint: disable=protected-access

# Imports
# Use any appropriate data structure here.
from List_array import List

# Constants
SEP = '-' * 40


class Hash_Set:
    """
    -------------------------------------------------------
    Constants.
    -------------------------------------------------------
    """
    _LOAD_FACTOR = 20

    def __init__(self, capacity):
        """
        -------------------------------------------------------
        Initializes an empty Hash_Set of size capacity.
        Use: hs = Hash_Set(capacity)
        -------------------------------------------------------
        Parameter:
            capacity - size of initial table in Hash Set  (int > 0)
        Returns:
            A new Hash_Set object (Hash_Set)
        -------------------------------------------------------
        """
        self._capacity = capacity
        self._table = []
        self._count = 0

        # Define the empty table.
        for _ in range(self._capacity):
            self._table.append(List())

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the number of values in the Hash Set.
        Use: n = len(hs)
        -------------------------------------------------------
        Returns:
            the number of values in the Hash Set.
        -------------------------------------------------------
        """
        return self._count

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the Hash Set is empty.
        Use: b = hs.is_empty()
        -------------------------------------------------------
        Returns:
            True if the Hash Set is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._count == 0

    def _find_slot(self, key):
        """
        -------------------------------------------------------
        Returns the slot for a key value.
        Use: list = hs._find_slot(key)
        -------------------------------------------------------
        Returns:
            slot - list at the position of hash key in self._table
        -------------------------------------------------------
        """
        value = hash(key) % self._capacity
        slot = self._table[value]
        return slot

    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Determines if the Hash Set contains key.
        Use: b = key in hs
        -------------------------------------------------------
        Parameters:
            key - a comparable data element (?)
        Returns:
            True if the Hash Set contains key, False otherwise.
        -------------------------------------------------------
        """
        # your code here
        found = False
        crypt = hash(key)
        slot = crypt % self._capacity
        if not self._table[slot].is_empty():
            i = self._table[slot].index(key)
            if i != -1:
                found = True
        return found

    def insert(self, value):
        """
        ---------------------------------------------------------
        Inserts value into the Hash Set, allows only one copy of value.
        Calls _rehash if the Hash Set _LOAD_FACTOR is exceeded.
        Use: inserted = hs.insert(value)
        -------------------------------------------------------
        Parameters:
            value - a comparable data element (?)
        Returns:
            inserted - True if value is inserted, False otherwise.
        -------------------------------------------------------
        """
        # your code here
        inserted = False
        crypt = hash(value)
        slot = crypt % self._capacity
        if not self._table[slot].is_empty():
            i = self._table[slot].index(value)
            if i == -1:
                self._table[slot].append(value)
                self._count += 1
                inserted = True
        else:
            self._table[slot].append(value)
            self._count += 1
            inserted = True
        if self._count / self._capacity > self._LOAD_FACTOR:
            self._rehash()
        return inserted

    def find(self, key):
        """
        ---------------------------------------------------------
        Returns the value identified by key.
        Use: value = hs.find(key)
        -------------------------------------------------------
        Parameters:
            key - a comparable data element (?)
        Returns:
            value - if it exists in the Hash Set, None otherwise.
        -------------------------------------------------------
        """
        # your code here
        value = None
        crypt = hash(key)
        slot = crypt % self._capacity
        if not self._table[slot].is_empty():
            i = self._table[slot].index(key)
            if i != -1:
                value = self._table[slot][i]
        return value

    def remove(self, key):
        """
        ---------------------------------------------------------
        Removes the value matching key from the Hash Set, if it exists.
        Use: value = hs.remove(key)
        -------------------------------------------------------
        Parameters:
            key - a comparable data element (?)
        Returns:
            value - if it exists in the Hash Set, None otherwise.
        -------------------------------------------------------
        """
        # your code here
        value = None
        crypt = hash(key)
        slot = crypt % self._capacity
        if not self._table[slot].is_empty():
            i = self._table[slot].index(key)
            if i != -1:
                value = self._table[slot].pop(i)
                self._count -= 1
        return value

    def _rehash(self):
        """
        ---------------------------------------------------------
        Increases the number of slots in the Hash Set and reallocates the
        existing data within the Hash Set to the new table.
        Use: hs._rehash()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        # your code here
        self._capacity = (2 * self._capacity) + 1
        new_table = []
        for _ in range(self._capacity):
            new_table.append(List())
        for slots in self._table:
            for value in slots:
                crypt = hash(value) % self._capacity
                new_table[crypt].append(value)
        self._table = new_table
        return

    def __eq__(self, target):
        """
        ----------------
        Determines whether two Hash_Sets are equal.
        Values in self and target are compared and if all values are equal
        and in the same order, returns True, otherwise returns False.
        Use: equals = source == target
        ---------------
        Parameters:
            target - a hash set (Hash_Set)
        Returns:
            equals - True if source contains the same values
                as target in the same order, otherwise False. (boolean)
        ---------------
        """
        # your code here
        equals = False
        if self._count == target._count:
            equals = True
            for i in range(self._capacity):
                if len(self._table[i]) != len(target._table[i]):
                    equals = False
                    break
                for j in range(len(self._table[i])):
                    if self._table[i][j] != target._table[i][j]:
                        equals = False
                        break
        return equals

    def debug(self):
        """
        USE FOR TESTING ONLY
        ---------------------------------------------------------
        Prints the contents of the Hash Set starting at slot 0,
        showing the slot currently being printed. Used for
        debugging purposes.
        Use: hs.debug()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        # your code here
        print(f"{len(self._table)} Slots")
        print()
        print("----------------------------------------")
        for index in range(len(self._table)):
            print(f"Slot {index}")
            print()
            for value in self._table[index]:
                print(value)
                print()
        return

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the hash set
        from first to last slots. Assumes slot has own iterator.
        Use: for v in q:
        -------------------------------------------------------
        Returns:
            yields
            value - the next value in the list (?)
        -------------------------------------------------------
        """
        for slot in self._table:
            for item in slot:
                yield item
