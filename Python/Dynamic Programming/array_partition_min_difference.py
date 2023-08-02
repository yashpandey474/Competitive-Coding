from os import *
from sys import *
from collections import *
from math import *

from sys import stdin, stdout, setrecursionlimit

setrecursionlimit(10 ** 7)

def minSubsetSumDifference(arr, n):
    # Write your code here.
    # Return the minimum difference in the form of an integer.
    
    #TOTAL SUM
    total_sum = sum(arr)

    #CACHE
    cache = {}
    n = len(arr)

    #DFS FUNCTION
    def dfs(index, current):
        #ALL CONSIDERED
        if index >= n:
            if current != total_sum:
                return abs((total_sum - current) - current)
            return float('inf')

        #ALREADY CACHED
        if (index, current) in cache:
            return cache[(index, current)]

        #SUSBET
        res = min(
            dfs(index + 1, current),
            dfs(index + 1, current + arr[index])
        )
        cache[(index, current)] = res
        return res
    return dfs(0, 0)









# Taking input using fast I/0.
def takeInput():
    N = int(input())
    arr = list(map(int, input().split()))
    return len(arr), arr

tc = 1
while tc > 0:
    N, arr = takeInput()
    ans = minSubsetSumDifference(arr, N)
    stdout.write(str(ans) + "\n")
    tc -= 1
