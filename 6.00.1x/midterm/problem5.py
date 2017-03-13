# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 16:34:51 2017

@author: Avokald
"""


def dotProduct(listA, listB):
    summ = 0
    for i in range(len(listA)):
        summ += listA[i] * listB[i]
    return summ


def main():
    listA = [1, 2, 3, 4]
    listB = [5, 6, 7, 8]
    print(dotProduct(listA, listB))


if __name__ == "__main__":
    main()
