def range20():
    i = 0
    while i < 20:
        yield i
        i += 1

if __name__ == "__main__":
    # map the str function onto every item returned by the iterator and return
    # an iterable giving them back out
    m = map(str, range20())

    # join items returned by an iterator
    s = "".join(m)
    print(s)
