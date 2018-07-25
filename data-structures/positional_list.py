from exceptions import EmptyError
from doubly_linked_base import _DoublyLinkedBase

# todo:
# what happens when the header or trailer is passed to the methods
class PositionalList(_DoublyLinkedBase):

    # position abstraction
    class Position:

        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node._element

        # see alternative function isinstance()
        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            return not (self == other)

    def _validate(self, p):
        # also handles case where p == None
        if not isinstance(p, self.Position):
            raise TypeError("Must be a PositionalList.Position type.")

        if p._container is not self:
            raise ValueError("Position does not belong to this container.")

        if p._node._next is None:
            raise ValueError("Position is no longer valid.")

        return p._node

    # returns None when node is the header or trailer
    def _make_position(self, node):
        if node is self._header or node is self._trailer:
            return None
        return self.Position(self, node)

    # first position or None if empty
    def first(self):
        return self._make_position(self._header._next)

    # last position or None if empty
    def last(self):
        return self._make_position(self._trailer._prev)

    # position before or None if first
    def before(self, p):
        node = self._validate(p)
        return self._make_position(node._prev)

    # position after or None if last
    def after(self, p):
        node = self._validate(p)
        return self._make_position(node._next)

    # generator function which returns an iterable
    def __iter__(self):
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    # override to return position
    def _insert_between(self, e, prevNode, nextNode):
        node = super()._insert_between(e, prevNode, nextNode)
        return self._make_position(node)

    def add_first(self, e):
        return self._insert_between(e, self._header, self._header._next)

    def add_last(self, e):
        return self._insert_between(e, self._trailer._prev, self._trailer)

    def add_before(self, p, e):
        node = self._validate(p)
        return self._insert_between(e, node._prev, node)

    def add_after(self, p, e):
        node = self._validate(p)
        return self._insert_between(e, node, node._next)

    # unpack position and call derived method on node
    def delete(self, p):
        node = self._validate(p)
        return self._delete_node(node)

    # replace position's node element with e
    def replace(self, p, e):
        node = self._validate(p)
        old = node._element
        node._element = e
        return old

    def remove_first(self):
        if self.is_empty():
            raise EmptyError("PositionalList is empty")
        return super()._delete_node(self._header._next)

    def remove_last(self):
        if self.is_empty():
            raise EmptyError("PositionalList is empty")
        return super()._delete_node(self._trailer._prev)


def insertion_sort(L):
    # trivially sorted
    if len(L) <= 1:
        return

    # start from left
    border = L.first()

    # still nodes to sort
    while border != L.last():
        # next node to  insert
        current = L.after(border)
        e = current.element()

        # not necessary to insert
        if e > border.element():
            border = current
        # find leftmost node greater than current node
        else:
            # known leftmost node greater than the current node
            leftmost = border
            while leftmost != L.first() and L.before(leftmost).element() > e:
                leftmost = L.before(leftmost)
            L.delete(current)
            L.add_before(leftmost, e)

if __name__ == "__main__":

    pl = PositionalList()
    pl.add_last(10)
    pl.add_last(5)
    pl.add_last(13)
    pl.add_last(11)
    pl.add_last(9)
    pl.add_last(1)

    insertion_sort(pl)
    for e in pl:
        print(e)

    p = pl.first()
    h = pl.before(p)
    pl.add_before(h, -1)
