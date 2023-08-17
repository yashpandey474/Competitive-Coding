from os import *
from sys import *
from collections import *
from math import *

from typing import List


def countSquares(n: int, m: int, arr: List[List[int]]):
    #CREATE CACHE
    cache = {}

    #GET DIMENSIONS
    rows, cols = n, m

    def dfs(row, col):
        #INVALID
        if row >= rows or col >= cols:
            return 0

        #NOT A 1
        if arr[row][col] == 0:
            cache[(row, col)] = 0
            return 0

        #CHECK ALL 3 SIDES BELOW
        else:
            #TAKE MINIMUM OF 3
            res = 1 + min(dfs(row + 1, col + 1), dfs(row + 1, col), dfs(row, col + 1))
            cache[(row, col)] = res

            return res

    total_submatrices = 0
    for i in range(rows):
        for j in range(cols):
            total_submatrices += dfs(i, j)

    return total_submatrices
n, m = map(int, input().split())
arr = []
for i in range(n):
    row = list(map(int, input().split()))
    arr.append(row)

print(countSquares(n, m, arr))
quit()

        
