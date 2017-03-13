# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 14:03:34 2017

@author: Avokald
"""


def fancy_divide(list_of_numbers, index):
    denom = list_of_numbers[index]
    return [simple_divide(item, denom) for item in list_of_numbers]


def simple_divide(item, denom):
    try:
        return item / denom
    except ZeroDivisionError:
        return 0


def main():
    print(fancy_divide([0, 2, 4], 0))


if __name__ == "__main__":
    main()
