from exceptions import EmptyError

# stack implemented by way of a singly linked list
class LinkedStack:

    # singly linked node intended for private use
    class _Node:

        __slots__ = "_element", "_next"

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, element):
        self._head = LinkedStack._Node(element, self._head)
        self._size += 1

    def top(self):
        if self.is_empty():
            raise EmptyError("Stack is empty.")
        return self._head._element

    def pop(self):
        if self.is_empty():
            raiseEmptyError("Stack is empty.")
        e = self._head._element
        self._head = self._head._next
        self._size -= 1
        return e
