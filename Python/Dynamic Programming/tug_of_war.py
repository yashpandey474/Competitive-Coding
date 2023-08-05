from os import *
from sys import *
from collections import *
from math import *

def tugOfWar(arr, n):

    # write your code here
    cache = {}
    total_sum = sum(arr)

    def dfs(index, current, size):
        if index >= len(arr):
            # print("CURRENT = ", current)
            #ODD LENGTH
            if n % 2:
                if size == (n + 1)//2 or size == (n - 1)//2:
                    return abs(current - (total_sum - current))

            else:
                if size == n // 2:
                    return abs(current - (total_sum - current))

            return float('inf')

        if (index, current, size) in cache:
            return cache[(index, current, size)]

        res = min(
            dfs(index + 1, current, size),
            dfs(index + 1, current + arr[index], size + 1)
        )
        cache[(index, current, size)] = res
        return res

    return dfs(0, 0, 0)
