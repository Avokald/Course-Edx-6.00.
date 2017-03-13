# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 20:11:26 2017

@author: Avokald
"""


def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing.
    In case of a tie for the longest run, choose the longest run
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run.
    """

    assert len(L) > 2
    runUp = []
    runDown = []
    winnerUp = []
    winnerDown = []
    for i in range(len(L)):
        try:
            if (len(runUp) == 0 and len(runDown) == 0) or L[i] == L[i-1]:
                runUp.append(L[i])
                runDown.append(L[i])
                continue

            if L[i] > L[i-1]:
                runUp.append(L[i])
                if sum(runDown) > sum(winnerDown):
                    winnerDown = runDown
                runDown = []
                runDown.append(L[i])
            elif L[i] < L[i-1]:
                runDown.append(L[i])
                if sum(runUp) > sum(winnerUp):
                    winnerUp = runUp
                runUp = []
                runUp.append(L[i])
        finally:
            if sum(runUp) > sum(winnerUp):
                    winnerUp = runUp
            if sum(runDown) > sum(winnerDown):
                    winnerDown = runDown
    winner = winnerUp if sum(winnerUp) > sum(winnerDown) else winnerDown
    return winner


def main():
    longest_run([10, 4, 3, 8, 3, 4, 5, 7, 7, 2])


if __name__ == "__main__":
    main()