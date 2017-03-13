# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 14:47:38 2017

@author: Avokald
"""


def f(i):
    return i + 2


def g(i):
    return i > 5


def applyF_filterG(L, f, g):
    temp = L[:]
    L.clear()
    for i in temp:
        if g(f(i)) is True:
            L.append(i)
    if len(L) > 0:
        return max(L)
    else:
        return -1


def main():
    L = [0, -10, 5, 6, -4]
    print(applyF_filterG(L, f, g))
    print(L)


if __name__ == "__main__":
    main()
