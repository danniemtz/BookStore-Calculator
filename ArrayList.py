import numpy as np
from Interfaces import List


class ArrayList(List):
    """
        ArrayList: Implementation of a List interface using Arrays. 
    """

    def __init__(self):
        """
        __init__: Initialize the state (array, n and j). 
        """
        self.n = 0
        self.j = 0
        self.a = self.new_array(1)

    def new_array(self, n: int) -> np.array:
        """
        new_array: Create a new array of size n
        Input:
            n: the size of the new array
        Return:
            An array of size n
        """
        return np.zeros(n, object)

    def resize(self):
        """
        resize: Create a new array and copy the old values. 
        """
        b = self.new_array(max(1, 2 * self.n))
        # for k in range(self.n):
        #     b[k] = self.a[k]  #self.a[(self.j + k) % len(self.a)]
        for k in range(self.n+1):
            b[k] = self.a[(self.j + k) % len(self.a)]
        self.a = b
        self.j = 0

    def get(self, i: int) -> object:
        """
        get: returns the element at position i
        Inputs:
            i: Index that is integer non negative and at most n
        """
        if i < 0 or i >= self.n:
            raise IndexError
        return self.a[(self.j + i) % len(self.a)]

    def set(self, i: int, x: object) -> object:
        """
        set: Set the value x at the index i.
        Inputs:
            i: Index that is integer non negative and at most n
            x: Object type, i.e., any object 
        """
        if i < 0 or i >= self.n:
            raise IndexError()
            # y = self.a[(i + self.j)%len(self.a)]
        self.a[(i + self.j)%len(self.a)] = x
        return x

    def append(self, x: object):
        self.add(self.n, x)

    def add(self, i: int, x: object):
        """
            add: shift one position all the items j>=i, insert an element 
            at position i of the list and increment the number of elements 
            in the list
            Inputs:
                i: Index that is integer non-negative and at most n
                x: Object type, i.e., any object
        """
        if i < 0 or i > self.n:
            raise IndexError()
        if self.n == len(self.a):
            self.resize()
        if i < self.n / 2:
            #self.j = (self.j - 1) % len(self.a)  # set this here before for loop
            for k in range(0, i):    # changed position of 1 to opposite side and made it -1
                self.a[(self.j + k - 1) % len(self.a)] = self.a[(self.j + k) % len(self.a)]
            self.j = self.j - 1
        else:
            for k in range(self.n-1, i-1, -1):
                self.a[(self.j + k + 1) % len(self.a)] = self.a[(self.j + k) % len(self.a)]
        self.a[(self.j + i) % len(self.a)] = x
        self.n += 1

    def remove(self, i: int) -> object:
        if i < 0 or i >= self.n:
            raise IndexError()
        x = self.a[(self.j + i) % len(self.a)]
        if i < self.n/2:
            for k in range(i, 0, -1):  # changed from -1 to +1
                self.a[(self.j+k) % len(self.a)] = self.a[(self.j+k-1) % len(self.a)]
            self.j = (self.j + 1) % len(self.a)
        else:
            for k in range(i,self.n-1):
                self.a[(self.j+k) % len(self.a)] = self.a[(self.j+k+1) % len(self.a)]
        self.n -= 1
        if len(self.a) > 3*self.n:
            self.resize()
        return x

    def size(self) -> int:
        return self.n

    def __str__(self):
        s = "["
        for i in range(0, self.n):
            s += "%r" % self.a[(i + self.j) % len(self.a)]
            if i < self.n - 1:
                s += ","
        return s + "]"

    def __iter__(self):
        self.iterator = 0
        return self

    def __next__(self):
        if self.iterator < self.n:
            x = self.a[(self.iterator + self.j) % len(self.a)]
            self.iterator += 1
        else:
            raise StopIteration()
        return x

# TESTING
# def main():
#     arraylist = ArrayList()
#     arraylist.append("X")
#     arraylist.append("X")
#     arraylist.append("X")
#     arraylist.append("X")
#     arraylist.append("X")
#
#
#     arraylist.add(0, 'c')
#     arraylist.add(5, 'pp')
#     arraylist.add(5, 'oo')
#     arraylist.add(3, 'jj')
#     arraylist.add(4, 'ss')
#     arraylist.get(3)
#     arraylist.remove(4)
#     arraylist.get(3)
#     print(arraylist)
#     for i in arraylist:
#         print(i, end=' ')
#
#
# main()
