from os import *
from sys import *
from collections import *
from math import *


def recursion(n, target_sum, arr, current_index, current_sum):
    if current_index >= len(arr):
        if current_sum == target_sum:
            return True
        return False

    if current_sum > target_sum:
        return False

    #0/1 KNAPSACK
    return (recursion(n, target_sum, arr, current_index+1, current_sum + arr[current_index]) or 
    recursion(n, target_sum, arr, current_index+1, current_sum))
    

    
    
def subsetSumToK(n, k, arr):

    # Write your code here
    # Return a boolean variable 'True' or 'False' denoting the answer
    arr = sorted(arr)
    #NUMBER OF ELEMENTS; TARGET SUM; ARR; INDEX; CURRENT SUM
    return recursion(n, k, arr, 0, 0)
    
    
    

