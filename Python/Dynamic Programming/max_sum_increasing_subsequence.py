from os import *
from sys import *
from collections import *
from math import *

def maxIncreasingDumbbellsSum(rack, n):

    # Write your code here

    cache = {}
    
    def dfs(index, prev):
        if index >= len(rack):
            return 0

        if (index, prev) in cache:
            return cache[(index, prev)]

        res = dfs(index + 1, prev)
        if prev is None:
            res =  max(res, rack[index] + dfs(index + 1, rack[index]))

        elif rack[index] > prev:
            res =  max(res, rack[index] + dfs(index + 1, rack[index]))


        cache[(index, prev)] = res
        return res
    
    return dfs(0, None)

        

    
