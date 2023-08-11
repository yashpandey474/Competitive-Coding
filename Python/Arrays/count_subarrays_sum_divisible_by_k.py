from os import *
from sys import *
from collections import *
from math import *

def subArrayCount(arr, k):

    # Write your code here.
    # Return count of all the subarray that have sum is divisible by 'k'.
    
    #STANDARD ALGORITHM TO COUNT NUMBER OF SUBARRAYS
    prefix = 0
    count = 0
    #BASE CASE
    map_freq = {0: 1}


    for i in range(len(arr)):
        prefix = (prefix + arr[i]) % k

        #CHECK IF NEGATIVE
        if prefix < 0:
            prefix += k

        #CHECK IF IN MAP
        if prefix in map_freq:
            count += map_freq[prefix]
            map_freq[prefix] += 1
        
        else:
            map_freq[prefix] = 1

    return count

        
