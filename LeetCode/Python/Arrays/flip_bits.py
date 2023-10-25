from os import *
from sys import *
from collections import *
from math import *

def flipBits(arr, n): 
    # Write your code here
    max_total = 0
    cur_max = 0
    total_ones = 0


    for i in range(n):
        if arr[i] == 1:
            total_ones += 1
        val = (-1 if arr[i] == 1 else 1)
        cur_max = max(val, cur_max + val)
        max_total = max(max_total, cur_max)

    return total_ones + max_total
