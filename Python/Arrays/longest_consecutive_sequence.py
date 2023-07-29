from math import *
from collections import *
from sys import *
from os import *

def lengthOfLongestConsecutiveSequence(arr, n):
    # Write your code here.
    
    #SORT THE ARRAY
    arr = sorted(arr)
    len_seq = 1
    max_len = 1
    #ITERATE WHILE CONDITION SATISFIED
    for i in range(1, len(arr)):
        if arr[i-1] == arr[i] - 1:
            len_seq += 1
            max_len = max(max_len, len_seq)
        elif arr[i-1] == arr[i]:
            continue
        else:
            len_seq = 1
    return max_len
        
