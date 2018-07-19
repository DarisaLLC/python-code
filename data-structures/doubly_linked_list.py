#!/usr/bin/env python3

class _DoublyLinkedBase:

    class _Node:

        __slots__ = "_element", "_next", "_prev"

        def __init__(self, element, next, prev):
            self._element = element
            self._next = next
            self._prev = prev

    def __init__(self):
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _insert_between(self, e, prevNode, nextNode):
        node = self._Node(e, nextNode, prevNode)
        prevNode._next = node
        nextNode._prev = node
        self._size += 1
        return node

    def _delete_node(self, node):
        e = node._element
        node._prev._next = node._next
        node._next._prev = node._prev
        self._size -= 1

        # apparently this helps python's garbage collector
        node._prev = None
        node._next = None
        node._element = None

        return e
