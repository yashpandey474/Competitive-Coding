from os import *
from sys import *
from collections import *
from math import *

def lcs(str1, str2):
    # Write your code here.
    
    #CREATE A CACHE
    
    len1 = len(str1)
    len2 = len(str2)
    dp = [[0]*(len2 + 1) for i in range(len1 + 1)]
    max_length = 0

    #CREATE A DFS FUNCTION
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                max_length = max(max_length, dp[i][j])


    return max_length
