"""Implementations of some sorting"""
import random

from Interfaces import List


def linear_search(a: List, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return None
    #pass


def binary_search(a: List, x):
    l_bound = 0
    r_bound = len(a) - 1
    while l_bound <= r_bound:
        m = (l_bound+r_bound)//2
        if x == a[m]:
            return m
        elif x < a[m]:
            r_bound = m - 1
        else:
            l_bound = m+1
    return None


def _merge(a0: List, a1: List, a: List):
    i0 = 0
    i1 = 0

    for x in range(len(a)):
        if i0 == len(a0):
            a[x] = a1[i1]
            i1 += 1
        elif i1 == len(a1):
            a[x] = a0[i0]
            i0 += 1
        elif a0[i0] <= a1[i1]:
            a[x] = a0[i0]
            i0 += 1
        else:
            a[x] = a1[i1]
            i1 += 1
    #pass


def merge_sort(a):
    if len(a) <= 1:
        return a
    m = len(a) // 2
    a0 = a[0:m]
    a1 = a[m:len(a)]
    merge_sort(a0)
    merge_sort(a1)
    return _merge(a0, a1, a)
    #pass


def _partition(a:List, start, end):
    p = start
    for i in range(start+1, end+1):
        if a[i] <= a[start]:
            p += 1
            a[i], a[p], = a[p], a[i]
    a[p], a[start], = a[start], a[p]
    return p


def _quick_sort_f(a: List, start, end):
    if start < end:
        p = _partition(a, start, end)
        _quick_sort_f(a, start, p-1)
        _quick_sort_f(a, p+1, end)
    #pass


def _quick_sort_r(a: List, start, end):
    if start < end:
        p = _partition(a, start, end)
        _quick_sort_f(a, start, p-1)
        _quick_sort_f(a, p+1, end)
    #pass


def quick_sort(a: List, p=True):
    """
    sorts an ArrayList a using the quick sort algorithm.
    If parameter p is True, the quick sort algorithm uses a randomly chosen element from a as pivot.
    Otherwise, the quick sort algorithm uses the first element as pivot.
    """
    if p:
        _quick_sort_r(a, 0, a.size() - 1)
    else:
        _quick_sort_f(a, 0, a.size() - 1)
