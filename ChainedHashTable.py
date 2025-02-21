from Interfaces import Set
from DLList import DLList
import numpy as np


class ChainedHashTable(Set):
    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value

    def __init__(self, dtype=DLList):
        self.dtype = dtype
        self.d = 1
        self.t = self.alloc_table(2 ** self.d)
        self.z = 193759204821
        self.w = 31
        self.n = 0

    def alloc_table(self, n: int):
        t = np.zeros(n, dtype=object)
        for i in range(n):
            t[i] = self.dtype()
        return t

    def _hash(self, key: int) -> int:
        return self.z * hash(key) % (2 ** self.w) >> (self.w - self.d)

    def size(self) -> int:
        return self.n

    def find(self, key: object) -> object:
        bin = self._hash(key)
        for i in range(self.t[bin].size()):  # originally had -1 in range but it didnt work (try later)
            if self.t[bin].get(i).key == key:  # now it works but we will see if interferes with code later
                return self.t[bin].get(i).value
        return None

    def add(self, key: object, value: object):
        """add the item (key, val) to the table if key doesnt already exist"""
        if self.find(key) is not None:
            return False   # changed from False to None
        if self.n == len(self.t):
            self.resize()
        bin = self._hash(key)
        item = self.Node(key, value)
        self.t[bin].add(0, item)
        self.n += 1
        return True

    def remove(self, key: int) -> object:
        # bin = self._hash(key)
        # for i in range(len(self.t[bin])):
        #     if self.t[bin].get(i).key == key:
        #         y = self.find(key)
        #         self.t[bin].remove(i)
        #         self.n -= 1
        #         if len(self.t) > 3*self.n:
        #             self.resize()
        #         return y
        bin = self.t[self._hash(key)]
        for i in range(len(bin)):
            poo = bin.get(i)
            if poo.key == key:
                bin.remove(i)
                self.n -= 1
                if len(self.t) > 3*self.n:
                    self.resize()
                return True
        return None

    def resize(self):
        if self.n == len(self.t):
            self.d += 1
        else:
            self.d -= 1
        temp_variable = self.alloc_table(2 ** self.d)
        for j in range(len(self.t)):
            for i in range(self.t[j].size()):
                bin = self._hash(self.t[j].get(i).key)
                temp_variable[bin].add(0, self.t[j].get(i))
        self.t = temp_variable

    def __str__(self):
        s = "["
        for i in range(len(self.t)):
            for j in range(len(self.t[i])):
                k = self.t[i][j]
                s += str(k.key)
                s += ":"
                s += str(k.value)
                s += ";"
        return s + "]"


#testing
# x = ChainedHashTable()
# # x.remove(0)
#
#
# # x.add(2, "second")
# # x.add(1, "first")
# # x.add(3, "fourth")
# # x.add(4, "third")
# x.add(23, "A")
# x.add(15, "B")
# x.add(11, "C")
# x.remove(23)
# x.remove(15)
# x.add(10, "D")
# x.add(12, "A")
#
#
# # y = x.find(2)
# print(x)
#
# # print(y)
