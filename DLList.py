from Interfaces import List
import numpy as np


class DLList(List):
    class Node:
        def __init__(self, x: object):
            self.next = None
            self.prev = None
            self.x = x

    def __init__(self):
        self.dummy = DLList.Node("")
        self.dummy.next = self.dummy
        self.dummy.prev = self.dummy
        self.n = 0

    def get_node(self, i: int) -> Node:
        if i < 0 or i >= self.n:
            return self.dummy
        if i < self.n/2:
            p = self.dummy.next
            for k in range(i):
                p = p.next  # check this out
        else:
            p = self.dummy   # took out .prev and changed range from n-i-1
            for k in range(self.n - i):
                p = p.prev
        return p
        #pass

    def get(self, i) -> object:
        if i < 0 or i >= self.n:
            raise IndexError()
        return self.get_node(i).x
        #pass

    def set(self, i: int, x: object) -> object:
        if i < 0 or i >= self.n:
            raise IndexError()
        node = self.get_node(i)
        old = node.x
        node.x = x
        return old
        #pass

    def add_before(self, w: Node, x: object) -> Node:  # w is the node, x is the data
        if w == None:
            raise Exception("")  # maybe raise IndexError()
        u = self.Node(x)
        u.prev = w.prev
        u.next = w
        w.prev = u
        u.prev.next = u
        self.n += 1
        return u
        #pass

    def add(self, i: int, x: object):
        if i < 0 or i > self.n:
            return IndexError()
        return self.add_before(self.get_node(i), x)
        #pass

    def _remove(self, w: Node):
        if self.n == 0:
            raise IndexError()
        w.prev.next = w.next
        w.next.prev = w.prev
        self.n -= 1
        return w.x
        
        #pass

    def remove(self, i: int):
        if i < 0 or i > self.n:
            raise IndexError()
        return self._remove(self.get_node(i))

    def size(self) -> int:
        return self.n

    def append(self, x: object):
        self.add(self.n, x)

    def isPalindrome(self) -> bool:

        if self.n <= 1:   # if the input was just A, forward and backwards is just A == True
            return True
        left = self.dummy.next  # this is the first in list
        right = self.dummy.prev    # last in list
        while left != right and left.prev != right:  # to start at opp ends and stop once reach same node
            if left.x != right.x:  # if they are different --> not palindrome
                return False
            left = left.next  # shifting forward and back(right node) until reaches middle
            right = right.prev
        return True
        #pass

    def reverse(self):
        first = self.dummy.next
        last = self.dummy.prev

        for i in range(int(self.n/2)):
            temp_node = first.x   # front node data
            first.x = last.x
            last.x = temp_node
            first = first.next   # shifting forward each time
            last = last.prev  # shifting back each time

    def __str__(self):
        s = "["
        u = self.dummy.next
        while u is not self.dummy:
            s += "%r" % u.x
            u = u.next
            if u is not None:
                s += ","
        return s + "]"

    def __iter__(self):
        self.iterator = self.dummy.next
        return self

    def __next__(self):
        if self.iterator != self.dummy:
            x = self.iterator.x
            self.iterator = self.iterator.next
        else:
            raise StopIteration()
        return x
