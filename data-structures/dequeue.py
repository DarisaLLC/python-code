from exceptions import EmptyError
from doubly_linked_base import _DoublyLinkedBase

class LinkedDequeue(_DoublyLinkedBase):

    def add_first(self, e):
        self._insert_between(e, self._header, self._header._next)

    def add_last(self, e):
        self._insert_between(e, self._trailer._prev, self._trailer)

    def remove_first(self):
        if self.is_empty():
            raise EmptyError("Dequeue is empty.")
        return self._delete_node(self._header._next)

    def remove_last(self):
        if self.is_empty():
            raise EmptyError("Dequeue is empty.")
        return self._delete_node(self._trailer._prev)

    def first(self):
        if self.is_empty():
            raise EmptyError("Dequeue is empty.")
        return self._header._next._element

    def last(self):
        if self.is_empty():
            raise EmptyError("Dequeue is empty.")
        return self._trailer._prev._element
