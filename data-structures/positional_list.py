from exceptions import EmptyError
from doubly_linked_list import _DoublyLinkedBase

class PositionalList:

    class Position:

        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node._element

        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            return not (self == other)

    def validate(self):
