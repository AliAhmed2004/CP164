# Imports
from copy import deepcopy


class _Deque_Node:

    def __init__(self, value, _prev, _next):
        """
        -------------------------------------------------------
        Initializes a deque node.
        Use: node = _Deque_Node(value, _prev, _next)
        -------------------------------------------------------
        Parameters:
            value - value value for node (?)
            _prev - another deque node (_Deque_Node)
            _next - another deque node (_Deque_Node)
        Returns:
            a new _Deque_Node object (_Deque_Node)

        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._prev = _prev
        self._next = _next


class Deque:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty deque.
        Use: d = deque()
        -------------------------------------------------------
        Returns:
            a new Deque object (Deque)
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0
        
    def _swap(self, l, r):
        if self._front == l and self._rear == r:
            self._front = r
            self._rear = l
        elif self._rear == l and self._front == r:
            self._rear = r
            self._front = l
        else:
            if l._next == r:
                if l._prev is None:
                    self._front = r
                else:
                    l._prev._next = r
                if r._next is None:
                    self._rear = l
                else:
                    r._next._prev = l
                l._next, r._prev = r, l
            elif r._next == l:
                if r._prev is None:
                    self._front = l
                else:
                    r._prev._next = l
                if l._next is None:
                    self._rear = r
                else:
                    l._next._prev = r
                l._prev, r._next = r, l
            else:
                l._prev._next, r._prev._next = r, l
                l._next._prev, r._next._prev = r, l
                l._prev, r._prev = r._prev, l._prev
                l._next, r._next = r._next, l._next
                