from os import *
from sys import *
from collections import *
from math import *

def maximiseSum(arr1, arr2, n, m):

    # Write your code here
    
    #CREATE MAPS OF INDICES
    map_1 = {a: i for i, a in enumerate(arr1)}
    map_2 = {b: i for i, b in enumerate(arr2)}


    #CREATE A CACHE
    cache = {}

    #CREATE A DFS FUNCTION
    def dfs(index, arr):
        if index >= (n if arr == 1 else m):
            return 0

        if (index, arr) in cache:
            return cache[(index, arr)]

        curr = (arr1 if arr == 1 else arr2)
        res = curr[index] + dfs(index + 1, arr)

        if arr == 1:
            if curr[index] in map_2:
                res = max(res, curr[index] + dfs(map_2[curr[index]] + 1, 2))

        else:
            if curr[index] in map_1:
                res = max(res, curr[index] + dfs(map_1[curr[index]] + 1, 1))

        cache[(index, arr)] = res
        return res

    return max(dfs(0, 1), dfs(0, 2))
        
