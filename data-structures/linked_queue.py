from exceptions import EmptyError

class LinkedQueue:

    class _Node:

        __slots__ = "_element", "_next"

        def __init__(self, element, next):
            self._element = element
            self._next = None

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def peek(self):
        if self.is_empty():
            raise EmptyError("Queue is empty.")
        return self._head._element

    def dequeue(self):
        if self.is_empty():
            raise EmptyError("Queue is empty.")
        e = self._head._element
        self._size -= 1
        self._head = self._head._next
        if self.is_empty():
            self._tail == None
        return e

    def enqueue(self, e):
        node = self._Node(e, None)

        if self.is_empty():
            self._head = node
        else:
            self._tail._next = node

        self._tail = node
        self._size += 1
