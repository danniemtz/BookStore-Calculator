import numpy as np
import ArrayStack

import BinaryTree
import ChainedHashTable
import DLList
import operator
import re


class Calculator:
    def __init__(self):
        self.dict = ChainedHashTable.ChainedHashTable()  # use to have a DLL list

    def set_variable(self, k: str, v: float):
        self.dict.add(k, v)

    def matched_expression(self, s: str) -> bool:
        stack = ArrayStack.ArrayStack()
        for x in s:
            if x == '(':
                stack.push(x)
            if x == ')':
                if len(stack) == 0:
                    return False
                else:
                    stack.pop()
        if len(stack) == 0:
            return True
        else:
            return False

    def _build_parse_tree(self, exp: str) -> BinaryTree:
        if self.matched_expression(exp) == False:
            raise ValueError
        tokens = []
        i = 0
        while i < len(exp):
            cur_tok = ""
            if exp[i].isalnum() == False:
                cur_tok = exp[i]
                tokens.append(cur_tok)
                i += 1
                continue
            while exp[i].isalnum() == True:
                cur_tok += exp[i]
                i += 1
            tokens.append(cur_tok)

        t = BinaryTree.BinaryTree()
        t.r = BinaryTree.BinaryTree.Node()
        current = t.r
        for tok in tokens:
            if tok == '(':
                #if current.left is None:
                current.insert_left(t.Node())
                current = current.left
            elif tok in ["+", "-", "/", "*"]:
                current.set_val(tok)
                current.set_key(tok)
                current.insert_right(t.Node())
                current = current.right
            elif tok.isalnum():
                current.set_key(tok)
                current.set_val(self.dict.find(tok))
                current = current.parent
            elif tok == ')':
                current = current.parent
        return t
        #pass

    def _evaluate(self, u):
        op = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}

        if u.left is not None and u.right is not None:
            fn = op[u.k]
            return fn(self._evaluate(u.left), self._evaluate(u.right))
        elif u.left is None and u.right is None:
            if u.v is not None:
                return u.v
            raise ValueError(f"Missing value for variable {u.k}")

        elif u.left is not None:
            return self._evaluate(u.left)
        else:
            return self._evaluate(u.right)

        #pass

    def evaluate(self, exp):
        parseTree = self._build_parse_tree(exp)
        return self._evaluate(parseTree.r)

    def print_expression(self, exp):
        if self.matched_expression(exp) == False:
            return False
        variable = r'[a-zA-Z]\w*'
        for variable in re.findall(variable, exp):
            if self.dict.find(variable) == None:
                exp = exp
            else:
                exp = exp.replace(variable, str(self.dict.find(variable)))
        return exp
