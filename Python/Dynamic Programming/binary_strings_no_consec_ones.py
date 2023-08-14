from os import *
from sys import *
from collections import *
from math import *

def numberOfBinaryStrings(n: int) -> int:
    #CREATE CACHE: WITH DEFAULT VALUES
    cache = {(1,  0): 1, (1, 1): 1}

    #DFS FUNCTION
    def dfs(length, curr):

        if (length, curr) in cache:
            return cache[(length, curr)]

        if curr == 0:
            res = dfs(length - 1, 0) + dfs(length - 1, 1)

        else:
            res =  dfs(length - 1, 0)

        cache[(length, curr)] = res%(10**9 + 7)
        return res%(10**9 + 7)
    #RETURN THE RESULT
    return (
        dfs(n, 0)
        + dfs(n, 1)
    )%(10**9 + 7)
