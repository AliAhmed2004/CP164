"""
-------------------------------------------------------
Array version of the Priority Queue ADT.
-------------------------------------------------------
Author:  Ali Ahmed
ID:      169038398
Email:   ahme8398@mylaurier.ca
Section: CP164 A
__updated__ = "2023-02-11"
-------------------------------------------------------
"""
from copy import deepcopy


class Priority_Queue:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty priority queue.
        Use: pq = Priority_Queue()
        -------------------------------------------------------
        Returns:
            a new Priority_Queue object (Priority_Queue)
        -------------------------------------------------------
        """
        self._values = []
        self._first = None
        self._items = []

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the priority queue is empty.
        Use: b = pq.is_empty()
        -------------------------------------------------------
        Returns:
            True if priority queue is empty, False otherwise.
        -------------------------------------------------------
        """
        return len(self._values) == 0

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the length of the priority queue.
        Use: n = len(pq)
        -------------------------------------------------------
        Returns:
            the number of values in the priority queue.
        -------------------------------------------------------
        """
        return len(self._values)

    def insert(self, value):
        """
        -------------------------------------------------------
        A copy of value is appended to the end of the the priority queue
        Python list, and _first is updated as appropriate to the index of
        value with the highest priority.
        Use: pq.insert(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        self._values.append(deepcopy(value))

        if self._first == None:
            self._first = 0

        else:
            if value < self._values[self._first]:
                self._first = len(self._values) - 1
        return

    def peek(self):
        """
        -------------------------------------------------------
        Peeks at the highest priority value of the priority queue.
        Use: v = pq.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the highest priority value in the priority queue -
                the value is not removed from the priority queue. (?)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot peek at an empty priority queue"

        value = deepcopy(self._values[self._first]) # type: ignore

        return value

    def remove(self):
        """
        -------------------------------------------------------
        Removes and returns the highest priority value from the priority queue.
        Use: value = pq.remove()
        -------------------------------------------------------
        Returns:
            value - the highest priority value in the priority queue -
                the value is removed from the priority queue. (?)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot remove from an empty priority queue"
        value = self._values[self._first] # type: ignore
        self._values = self._values[:self._first] + \
            self._values[self._first + 1:] # type: ignore
        self._set_first()
        return value

    def _set_first(self):
        """
        -------------------------------------------------------
        Private helper function to set the value of _first.
        _first is the index of the value with the highest
        priority in the priority queue. None if queue is empty.
        Use: self._set_first()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """

        n = len(self._values)

        if n == 0:
            self._first = None

        else:
            self._first = 0

        for i in range(1, n):
            if self._values[i] < self._values[self._first]: # type: ignore
                self._first = i

        return

    def __iter__(self):
        """
        FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the priority queue
        from front to rear. Not in priority order.
        Use: for value in pq:
        -------------------------------------------------------
        Returns:
            value - the next value in the priority queue (?)
        -------------------------------------------------------
        """
        for value in self._values:
            yield value

    def split_key(self, key):
        """
        -------------------------------------------------------
        Splits a priority queue into two depending on an external
        priority key. The source priority queue is empty when the method
        ends. The order of the values from source is preserved.
        Use: target1, target2 = source.split_key(key)
        -------------------------------------------------------
        Parameters:
            key - a data object (?)
        Returns:
            target1 - a priority queue that contains all values
                with priority higher than key (Priority_Queue)
            target2 - priority queue that contains all values with
                priority lower than or equal to key (Priority_Queue)
        -------------------------------------------------------
        """
        target1 = Priority_Queue()
        target2 = Priority_Queue()

        for i in self._values:
            if i < key:
                target1.insert(i)
            else:
                target2.insert(i)

        self._values = []
        self._first = None

        return target1, target2
    
    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source queues into the current target priority queue.
        When finished, the contents of source1 and source2 are inserted
        into target and source1 and source2 are empty.
        (iterative algorithm)
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an linked-based priority queue (Priority_Queue)
            source2 - an linked-based priority queue (Priority_Queue)
        Returns:
            None
        -------------------------------------------------------
        """
        while len(source1._values) > 0 and len(source2._values) > 0:
            self._values.append(source1._values.pop(0))
            self._values.append(source2._values.pop(0))
        while len(source1._values) > 0:
            self._values.append(source1._values.pop(0))
        while len(source2._values) > 0:
            self._values.append(source2._values.pop(0))
        source1._first = None
        source2._first = None
        self._set_first()
        return
        
    def split_alt(self):
        """
        -------------------------------------------------------
        Splits a priority queue into two. target1 contains the even indexed
        elements and target2 contains the odd indexed elements. The source
        priority queue is empty when the method ends.
        (iterative algorithm)
        Use: target1, target2 = source.split_alt()
        -------------------------------------------------------
        Returns:
            target1 - a priority queue that contains all even indexed
                elements of the source priority queue (Priority_Queue)
            target2 - a priority queue that contains all odd indexed
                elements of the source priority queue (Priority_Queue)
        -------------------------------------------------------
        """
        target1 = Priority_Queue()
        target2 = Priority_Queue()
        for i in range(len(self._values)):
            if i % 2 == 0:
                target1.insert(self._values[i])
            else:
                target2.insert(self._values[i])
        self._values = []  # empty the source list
        self._first = None
        return target1, target2