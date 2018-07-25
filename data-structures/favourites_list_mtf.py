from positional_list import PositionalList
from favourites_list import FavouritesList

class FavouritesListMtf(FavouritesList):

    def _move_up(self, p):
        if p != self._data.first():
             item = self._data.delete(p)
             self._data.add_first(item)

    def top(self, k):
        if k < 1 or k > len(self._data):
            raise ValueError("Invalid value for k.")

        tmp = PositionalList()
        for i in range(len(self._data)):
            tmp.add_first(self._data.delete(self._data.first()))

        for i in range(k):
            p = tmp.first()
            p_max = tmp.first()
            max = p.element()._value

            while p != None:
                if p.element()._value > max:
                    p = self._data.after(p)
                    p_max = p.element()
                    max = p_max._value

            yield max

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
