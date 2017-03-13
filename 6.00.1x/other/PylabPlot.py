# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 11:26:28 2017

@author: Avokald
"""

import pylab as plt
import math

array1 = []
array2 = []
for i in range(20):
    array1.append(math.sqrt(i))
    array2.append(i)
plt.figure('graph1')
plt.clf()
plt.plot(array2, array1, label='master')

plt.figure('graph2')
plt.clf()
plt.plot(array1, array2)

plt.figure('graph1')
plt.xlim(0, 15)
plt.legend(loc='upper center')
plt.xlabel('xs')
plt.ylabel('ys')
plt.title("Hello")
plt.figure('graph2')
plt.title("Oukuway")
