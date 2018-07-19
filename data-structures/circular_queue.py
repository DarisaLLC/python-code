from exceptions import EmptyError

class CircularQueue:

    class _Node:

        __slots__ = "_element", "_next"

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._size = 0
        self._tail = None

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def peek(self):
        if self.is_empty():
            raise EmptyError("Circular queue is empty.")
        return self._tail._next._element

    def rotate(self):
        if not self.is_empty():
            self._tail = self._tail._next

    def enqueue(self, e):
        node = self._Node(e, None)
        if self.is_empty():
            node._next = node
        else:
            node._next = self._tail._next
            self._tail._next = node
        self._tail = node
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise EmptyError("Circular queue is empty.")
        e = self._tail._next._element
        if self._size == 1:
            self._tail = None
        else:
            self._tail._next = self._tail._next._next
        self._size -= 1
        return e
