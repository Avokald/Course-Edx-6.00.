# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 16:39:34 2017

@author: Avokald
"""


def dict_interdiff(d1, d2):
    if len(d1) == len(d2):
        res1 = {}
        for i in list(d1.keys()):
            res1[i] = (d1[i] >= d2[i])
        return (res1, {})
    else:
        resu1 = {}
        resu2 = {}
        err1 = list(d1.keys())
        err2 = list(d2.keys())
        err3 = err1 + err2
        print(err1, err2, err3)
        for i in err3:
                    if i in d1 and i in d2:
                        resu1[i] = d1[i] + d2[i]
                    elif i in d1:
                        resu2[i] = d1[i]
                    elif i in d2:
                        resu2[i] = d2[i]
        return (resu1, resu2)


def main():
    print(dict_interdiff({1: 1, 2: 2, 3: 3, 4: 4, 5: 4}, \
                         {1: 1, 2: 2, 3: 3, 4: 5}))


if __name__ == "__main__":
    main()
