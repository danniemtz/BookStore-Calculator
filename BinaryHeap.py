import numpy as np
import math
from Interfaces import Queue
from Interfaces import Tree


def left(i: int) -> int:
    """
    helper method; returns the index of the left child of the element at index i
    """
    return 2 * i + 1
    #pass


def right(i: int) -> int:
    """
    helper method; returns the index of the right child of the element at index i
    """
    return 2 * (i + 1)
    #pass


def parent(i: int) -> int:
    """
    helper method; returns the index of the parent of the element at index i
    """
    return ((i -1) // 2)
    #pass


def _new_array(n: int) -> np.array:
    """
    helper method; creates a new numpy array of 0's of size n
    """
    return np.zeros(n, object)


class BinaryHeap(Queue, Tree):
    def __init__(self):
        self.a = _new_array(1)
        self.n = 0

    def add(self, x: object):
        if len(self.a) == self.n:
            self._resize()
        self.a[self.n] = x
        self.n += 1
        self._bubble_up_last()
        return True
        #pass

    def remove(self):
        if self.n == 0:
            raise IndexError
        x = self.a[0]
        self.a[0] = self.a[self.n - 1]
        self.n -= 1
        self._trickle_down_root()
        if 3 * self.n < len(self.a):
            #self._resize()
            pass
        return x
        #pass

    def depth(self, u) -> int:
        d = 0  # depth count
        current_node = u
        curr_idx = 0
        while self.a[curr_idx] != u:
            curr_idx += 1
            #break
        while self.a[curr_idx] != self.a[0]:
            curr_idx = parent(curr_idx)
            d += 1
        return d
    def height(self) -> int:
        return int(math.log2(self.n))

    def bf_order(self) -> list:
        nodes = []#BinaryHeap()
        #u = 0
        root = 0
         # getting these methods from binary tree but using attributes available
        while self.n > 0:   # so in binary tree, self.r (root) would be self.a[0] here
            if self.a[root] != None:
                nodes.append(self.a[root])
            #root = left(root)  # the root is now equal to the left child ( bc goes from left to right)

            self.n -= 1
            root += 1
        return nodes
        #pass

    def in_order(self) -> list:
        return self._in_order(0)
        #pass

    def _in_order(self, i):   # helper method
        first = self.a[0]
        u = self.a[i]
        nodes = []
        if left(i) <= self.n:
            nodes.extend(self._in_order(left(i)))
        if u >= first:
            nodes.append(u)  # changed from regular i to self.a[i]
        if right(i) <= self.n:
            nodes.extend(self._in_order(right(i)))
        return nodes

    def post_order(self) -> list:
        return self._post_order(0)  # self.a[0] is the root of the queue
        #pass

    def _post_order(self, i):  # helper method
        nodes = []
        u = self.a[i]
        first = self.a[0]
        if left(i) <= self.n:
            nodes.extend(self._post_order(left(i)))
        if right(i) <= self.n:
            nodes.extend(self._post_order(right(i)))
        if u >= first:
            nodes.append(u)
        return nodes

    def pre_order(self) -> list:
        return self._pre_order(0)
        #pass

    def _pre_order(self, i):  # helper method
        nodes = []
        u = self.a[i]
        first = self.a[0]
        if u >= first:  # changed from > to <
            nodes.append(u)
        if left(i) <= self.n:
            nodes.extend(self._pre_order(left(i)))
        if right(i) <= self.n:
            nodes.extend(self._pre_order(right(i)))
        return nodes

    def size(self) -> int:
        return self.n

    def find_min(self):
        if self.n == 0: raise IndexError()
        return self.a[0]

    def _bubble_up_last(self):
        i = self.n - 1   # initialize temp variable to be last index of the last element in heap
        p_idx = parent(i)
        while i > 0 and self.a[i] < self.a[p_idx]:
            x = self.a[i]
            self.a[i] = self.a[p_idx]  # swap a[i] with a[p_idx]
            self.a[p_idx] = x
            i = p_idx
            p_idx = parent(i)  # p_idx updated as parent of i
        #pass

    def _resize(self):
        b = _new_array(max(1, 2 * self.n))
        for k in range(self.n):
            b[k] = self.a[k]
        self.a = b
        #pass

    def _trickle_down_root(self):
        i = 0   # to be index of the element at root
        l_idx = left(i)  # left index is the left child and right (r_idx) is right child of i
        r_idx = right(i)
        while i < self.n and l_idx <= self.n and r_idx <= self.n and (self.a[i] > self.a[l_idx] or self.a[i]>self.a[r_idx]):
            min_ele = min(self.a[i], self.a[l_idx], self.a[r_idx])  # min is the minimum between parent and children
            if min_ele == self.a[i]:
                min_idx = i
            elif min_ele == self.a[l_idx]:  # if min_idx == to this value
                min_idx = l_idx  # then the index is this
            else:
                min_idx = r_idx
            a = self.a[i]
            y = self.a[min_idx]
            self.a[i] = y
            self.a[min_idx] = a
            i = min_idx
            l_idx = left(i)
            r_idx = right(i)

        #pass

    def __str__(self):
        return str(self.a[0:self.n])