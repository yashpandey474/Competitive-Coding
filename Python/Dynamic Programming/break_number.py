from os import *
from sys import *
from collections import *
from math import *

def breakNumber(n):
    # Write your code here.
    
    result = []
    cache = {}

    def dfs(number, answer, index):
        if number == 0:
            result.append(answer)

        if number < 0:
            return

        for i in range(index, number + 1):
            dfs(number - i, answer + [i], i)

    dfs(n, [], 1)
    return result
    
    
