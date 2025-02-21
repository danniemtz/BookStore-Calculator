from Interfaces import Graph, List
import ArrayList
import ArrayQueue
import ArrayStack
import numpy as np
"""An implementation of the adjacency list representation of a graph"""

class AdjacencyMatrix(Graph):

    def __init__(self, n : int):
        self.n = n
        self.adj = np.zeros((self.n, self.n), dtype=int)

    def add_edge(self, i : int, j : int):
        if i < 0 or i >= self.n or j < 0 or j >= self.n:
            raise IndexError
        self.adj[i][j] = True
        #pass

    def remove_edge(self, i : int, j : int):
        if i >= self.n or j >= self.n:
            raise IndexError
        if self.adj[i][j] == True:
            self.adj[i][j] = False
            return True
        return False

        #pass

    def has_edge(self, i : int, j: int) ->bool:
        if i < 0 or i >= self.n or j < 0 or j >= self.n:
            raise IndexError
        return self.adj[i][j]
        #pass

    def out_edges(self, i) -> List:
        ed = []
        for j in range(self.n):
            if self.adj[i][j] == 1:
                ed.append(j)
        return ed
        #pass

    def in_edges(self, j) -> List:
        ees = []
        for i in range(self.n):
            if self.adj[i][j] == 1:
                ees.append(i)
        return ees
        #pass

    def bfs(self, r : int):
        traversal = []
        seen = []
        for x in range(self.n):
            seen.append(False)

        q = ArrayQueue.ArrayQueue()
        q.add(r)
        traversal.append(r)
        seen[r] = True

        neigh = []
        while q.n != 0:
            current = q.remove()
            neighbors = self.out_edges(current)

            for j in range(self.n):
                if self.adj[current][j] != 0:
                    neigh.append(j)

            for x in neigh:
                if not seen[x]:
                    q.add(x)
                    traversal.append(x)
                    seen[x] = True
        return traversal
        #pass

    def dfs(self, r : int):
        traversal = []
        s = ArrayStack.ArrayStack()
        seen = []
        for x in range(self.n):
            seen.append(False)
        s.push(r)
        while s.n != 0:
            current = s.pop()
            if not seen[current]:
                traversal.append(current)
                seen[current] = True
            neighbors = []
            for n in range(self.n):
                if self.has_edge(current, n) == True:
                    neighbors.append(n)
            for neigh in neighbors[::-1]:
                if seen[neigh] == False:
                    s.push(neigh)
        return traversal
        #pass

    def size(self):
        return self.n

    def __str__(self):
        s = ""
        for i in range(0, self.n):
            s += "%i:  %r\n" % (i, self.adj[i].__str__())
        return s