from os import *
from sys import *
from collections import *
from math import *

def longestLengthString(matrix, n, m, string):
    # Write your code here
    # Return a list
    answer = [0]*len(string)
    rows = n
    cols = m

    cache = {}
    visited = set()

    def dfs(row, col, prev):
        if row < 0 or row >= rows or col < 0 or col >= cols or (row, col) in visited or matrix[row][col] != chr(ord(prev) + 1):
            return 0

        if (row, col) in cache:
            return cache[(row, col)]

        visited.add((row, col))
    
        res = 1 + max(
            dfs(row + 1, col, matrix[row][col]),
            dfs(row - 1, col, matrix[row][col]),
            dfs(row + 1, col + 1, matrix[row][col]),
            dfs(row + 1, col - 1, matrix[row][col]),
            dfs(row - 1, col + 1, matrix[row][col]),
            dfs(row - 1, col - 1, matrix[row][col]),
            dfs(row, col + 1, matrix[row][col]),
            dfs(row, col - 1, matrix[row][col]),
        )

        visited.remove((row, col))

        cache[(row, col)] = res
        return res

    #FOR EACH CHARACTER
    for i in range(len(string)):
        #FOR EACH ROW
        for r in range(rows):
            #FOR EACH COLUMN
            for c in range(cols):
                #STORE THE MAX LENGTH
                if matrix[r][c] == string[i]:
                    answer[i] = max(answer[i], dfs(r, c, chr(ord(string[i]) - 1)))

    #RETURN THE ARRAY
    return answer
