# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 13:51:17 2017

@author: Avokald
"""


def flatten(liste):
    forret = []
    cop = liste[:]

    def loope(cop):
        for i in cop:
            if type(i) == list:
                loope(i)
            else:
                forret.append(i)
    loope(cop)
    return forret


def main():
    liste = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]
    print(flatten(liste))


if __name__ == "__main__":
    main()
