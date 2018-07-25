from exceptions import EmptyError
from positional_list import PositionalList

# we maintain a collection of elements with individual access times
# this data structure uses a linked list sorted in non-increasing order of
# access count
#
# operations:
# - access(e)
# - remove(e)
# - top(k)
# - len()
# - is_empty()
#
# access an element by searching from most to least frequently accessed
# note we may need to walk an element towards the fron after it is accessed
#
# we use an underlying PositionalList for storage
# this is an example of the composition pattern, where a single object is
# composed of multiple other objects, allowing some implementation details to be
# abstracted
#
# specifically, we define a non-public nested class _Item which stores an
# element and and its access counts, the PositionalList is comprised of _Item
# instances

class FavouritesList:

    # positional list stores item intances
    class _Item:

        __slots__ = "_value", "_count"

        def __init__(self, e):
            self._value = e
            self._count = 0

    # return position of item with value e (items should have unique values)
    def _find_position(self, e):
        p = self._data.first()
        while p is not None and p.element()._value != e:
            p = self._data.after(p)
        return p

    # move position of newly inserted item up to the appropriate place
    def _move_up(self, p):
        if p == self._data.first():
            return

        it = self._data.before(p)

        if it.element()._count >= p.element()._count:
            return

        while self._data.before(it) != None and self._data.before(it).element()._count < p.element()._count:
            it = self._data.before(it)

        item = self._data.delete(p)
        self._data.add_before(it, item)

        # if p == self._data.first():
        #     return
        #
        # b = self._data.before(p)
        # c = p._element()._count
        #
        # while b.element()._count < c and self._data.before(b) != None:
        #     b = self._data.before(b)
        #
        # e = self.data.delete(p)
        #
        # if b.element()._count < c:
        #     self._data.add_before(b, e)
        # else:
        #     self._data.add_after(b, e)

    def __init__(self):
        self._data = PositionalList()

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def access(self, e):
        p = self._find_position(e)

        if p is None:
            p = self._data.add_last(self._Item(e))

        p.element()._count += 1
        self._move_up(p)

    def remove(self, e):
        p = self._find_position(e)
        if p is not None:
            self._data.delete(p)

    def top(self, k):
        if k < 1 or k > len(self._data):
            raise ValueError("Invalid value for k.")

        p = self._data.first()

        for i in range(k):
            yield p.element()._value
            p = self._data.after(p)

if __name__ == "__main__":
    f = FavouritesList()

    f.access("a")
    f.access("b")
    f.access("c")

    f.access("a")
    f.access("a")
    f.access("c")
    f.access("c")
    f.access("a")

    f.access("d")
    f.access("b")
    f.access("b")
    f.access("b")
    f.access("b")
    f.access("c")
    f.access("c")

    print(len(f))

    for s in f.top(3):
        print(s)
