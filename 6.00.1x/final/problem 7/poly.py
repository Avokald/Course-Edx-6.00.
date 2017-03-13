# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 14:57:06 2017

@author: Avokald
"""


def general_poly(L):
    def func(n):
        result = 0
        lenList = len(L)
        for i in range(lenList):
            result += L[i] * (n**((lenList - 1) - i))
        return result
    return func


def main():
    print(general_poly([1, 2, 3, 4])(8))


if __name__ == "__main__":
    main()
