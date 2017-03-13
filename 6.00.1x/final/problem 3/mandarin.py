# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 19:33:51 2017

@author: Avokald
"""


def convert_to_mandarin(us_num):
    '''
    us_num, a string representing a US number 0 to 99
    returns the string mandarin representation of us_num
    '''
    trans = {
    '0': 'ling', '1': 'yi', '2': 'er',
    '3': 'san',  '4': 'si', '5': 'wu',
    '6': 'liu',  '7': 'qi', '8': 'ba',
    '9': 'jiu', '10': 'shi'
    }
    us_num = str(us_num)
    copyNum = int(us_num)

    tens = str(copyNum // 10)
    ones = str(copyNum % 10)

    assert copyNum >= 0 and copyNum < 100

    if copyNum < 10:
        return trans[us_num]
    elif copyNum >= 10 and copyNum < 20:
        return trans['10'] + (" " \
        + trans[ones] if copyNum % 10 != 0 else "")
    else:
        return trans[tens] \
        + " " + trans['10'] \
        + (" " + trans[ones] if copyNum % 10 != 0 else "")
