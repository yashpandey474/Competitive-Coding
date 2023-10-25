from os import *
from sys import *
from collections import *
from math import *

def longestRepeatingSubsequence(st, n):

    #LRS WHERE NO INDEX IS SAME
    cache = {}

    if n <= 1:
        return 0

    def dfs(index1, index2):
        if (index1, index2) in cache:
            return cache[(index1, index2)]

        if index1 >= n or index2 >=n:
            return 0

        res = 0
        if st[index1] == st[index2] and index1 != index2:
            res = 1 + dfs(index1 + 1, index2 + 1)

        else:
            res = max(dfs(index1 + 1, index2), dfs(index1, index2 + 1))

        cache[(index1, index2)] = res
        return res

    return dfs(0, 0)

