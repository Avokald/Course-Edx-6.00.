# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 15:47:16 2017

@author: Avokald
"""


def closest_power(base, num):
    indexsu = 0
    diffe = 100000
    while True:
        temp = abs((base ** indexsu) - num)
        print(diffe, indexsu)
        if temp < diffe:
            diffe = temp
            indexsu += 1
        else:
            return indexsu - 1


def main():
    print(closest_power(5, 375.0))


if __name__ == "__main__":
    main()
