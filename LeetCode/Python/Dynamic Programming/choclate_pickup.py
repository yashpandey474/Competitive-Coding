from os import *
from sys import *
from collections import *
from math import *

from typing import List


def maximumChocolates(r: int, c: int, grid: List[List[int]]) -> int:
    # write your code here
    cache = {}
    #GET DIMENSIONS
    rows, cols = len(grid), len(grid[0])

    def dfs(row, col1, col2):
        #CHECK IF VALID
        if row < 0 or col1 < 0 or col2 <0 or col1>= cols or col2 >= cols or row >= rows:
            return 0

        #CHECK IF ALREADY CACHED
        if (row, col1, col2) in cache:
            return cache[(row, col1, col2)]

        maxChocolates = -float('inf')

        #FOR EVERY COLUMN ALICE CAN MOVE TO
        for i in range(-1, 2):
            #FOR EVERY COLUMN BOB CAN MOVE TO
            for j in range(-1, 2):
                #TAKE MAXIMUM
                maxChocolates = max(
                    maxChocolates,
                    dfs(row + 1, col1 + i, col2 + j)
                )
        #ONLY ADD CHOCOLATES IF NOT SAME COLUMN
        if col1 != col2:
            maxChocolates += grid[row][col2]
        #ADD CHOCOLATES FROM FIRST COLUMN
        cache[(row, col1, col2)] = maxChocolates + grid[row][col1]
        #RETURN VALUE
        return cache[(row, col1, col2)]

    return dfs(0, 0, cols-1)
