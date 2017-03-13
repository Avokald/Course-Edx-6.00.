# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 19:37:57 2017

@author: Avokald
"""


def genPrimes():
    primes = []
    x = 2
    while True:
        checker = 0
        if len(primes) == 0:
            yield x
            primes.append(x)
            continue
        for i in primes:
            if x % i == 0:
                checker += 1
        if checker > 0:
            x += 1
            continue
        else:
            yield x
            primes.append(x)
            x += 1
