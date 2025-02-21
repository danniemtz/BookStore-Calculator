from BinaryTree import BinaryTree
from Interfaces import Set


class BinarySearchTree(BinaryTree, Set):

    def __init__(self):
        BinaryTree.__init__(self)
        self.n = 0

    def add(self, key: object, value: object = None) -> bool:
        """
        If the key does not exist in this BinarySearchTree,
        adds a new node with given key and value, in the correct position.
        Returns True if the key-value pair was added to the tree, False otherwise.
        """
        new_node = self.Node(key, value)
        parent = self._find_last(key)
        return self._add_child(parent, new_node)
        #pass

    def find(self, key: object) -> object:
        """
        returns the value corresponding to the given key if the key
        exists in the BinarySearchTree, None otherwise
        """
        node = self._find_eq(key)
        if node == None:
            return None
        return node.v  # node value
        #pass

    def remove(self, key: object):
        """
        removes the node with given key if it exists in this BinarySearchTree.
        Returns the value corresponding to the removed key, if the key was in the tree.
        If given key does not exist in the tree, ValueError is raised.
        """
        u = self._find_eq(key)
        if u == None:
            raise ValueError
        value = u.v
        self._remove_node(u)
        return value
        #pass

    def _find_eq(self, key: object) -> BinaryTree.Node:
        """
        helper method; returns the node in this tree that contains the given key,
        None otherwise.
        """
        current = self.r
        while current != None:
            if key < current.k:
                current = current.left
            elif key > current.k:
                current = current.right
            else:
                return current
        return None
        #pass

    def _find_last(self, key: object) -> BinaryTree.Node:
        """
        helper method; returns the node in this tree that contains the given key, if it exists.
        Otherwise, returns the node that would have been the parent of the node
        with the given key, if it existed
        """
        current = self.r
        parent = None
        while current != None:
            parent = current
            if key < current.k:
                current = current.left
            elif key > current.k:
                current = current.right
            else:
                return current
        return parent
        #pass

    def _add_child(self, p: BinaryTree.Node, u: BinaryTree.Node) -> bool:
        """
        helper method; adds node u as the child of node p, assuming node p has at most 1 child
        """
        if p == None:
            self.r = u
        else:
            if u.k < p.k:
                p.left = u
            elif u.k > p.k:
                p.right = u
            else:
                return False
            u.parent = p
        self.n += 1
        return True
        #pass

    def _splice(self, u: BinaryTree.Node):
        """
        helper method; links the parent of given node u to the child
        of node u, assuming u has at most one child
        """
        if u.left != None:
            child = u.left
        else:
            child = u.right
        if u == self.r:
            self.r = child
            p = None
        else:
            p = u.parent
            if p.left == u:
                p.left = child
            else:
                p.right = child
        if child != None:
            child.parent = p
        self.n -= 1
        #pass

    def _remove_node(self, u: BinaryTree.Node):
        if u.left is None or u.right is None:
            self._splice(u)
        else:
            w = u.right
            while u.left != None:
                w = w.left
            u.k = w.k
            u.v = w.v
            self._splice(w)
        #pass

    def clear(self):
        """
        empties this BinarySearchTree
        """
        self.r = None
        self.n = 0

    def __iter__(self):
        u = self.first_node()
        while u is not None:
            yield u.k
            u = self.next_node(u)

    def first_node(self):
        w = self.r
        if w is None: return None
        while w.left is not None:
            w = w.left
        return w

    def next_node(self, w):
        if w.right is not None:
            w = w.right
            while w.left is not None:
                w = w.left
        else:
            while w.parent is not None and w.parent.left != w:
                w = w.parent
            w = w.parent
        return w

    def find_node(self, key):
        """this is to get the key == to input key, or the next Greater key closest to iinput key"""
        current = self.r
        smallest = None
        while current is not None:
            if key < current.k:
                smallest = current
                current = current.left
            elif key > current.k:
                current = current.right
            else:
                return current
        return smallest







