# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 13:39:41 2017

@author: Avokald
"""


import string

secretWord = 'aple'
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']

temp = string.ascii_lowercase
d = [str(i) for i in temp]

for i in lettersGuessed:
    if i in d:
        d.remove(i)
rt = ""
rt = rt.join(d)
return rt
