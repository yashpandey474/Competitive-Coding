from os import *
from sys import *
from collections import *
from math import *

from sys import stdin, stdout



def findMinCost(arr, n):
    # Write your code here.
    # Return an integer denoting the minimum cost.
    cache = {}

    def dfs(start, end):
        # CHECK IF IN CACHE
        if (start, end) in cache:
            return cache[(start, end)]

        # CHECK IF ONLY ONE ELEMENT
        if (start == end):
            cache[(start, end)] = 0
            return 0

        #SET TO INFINITY
        cache[(start, end)]= float('inf')
        #ELEMENTS IN RANGE
        sum_elements = sum(arr[start:end+1])

        #ITERATE FOR ALL POSSIBLE COMBINATIONS
        for k in range(start, end):
            cache[(start, end)] = min(
                cache[(start, end)],
                #START TO K        K TO END        SUM OF START TO END
                dfs(start, k) + dfs(k + 1, end) + sum_elements
            )
        return cache[(start, end)]

    return dfs(0, n-1)
        
