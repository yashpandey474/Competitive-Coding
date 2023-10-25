from os import *
from sys import *
from collections import *
from math import *

def minimumRemovals(arr, n, k):

    '''
    Write your code here.
    
    Return the minimum number of elements that should be removed
    from ARR (possibly zero) such that the difference between the
    maximum element and the minimum element of the remaining array
    is less than or equal to K.
    '''
	
    cache = {}

    def dfs(arr):
        if len(arr) == 0:
            return float('inf')

        if tuple(arr) in cache:
            return cache[tuple(arr)]

        if max(arr) - min(arr) <= k:
            return 0

        else:
            arr1 = arr[:]
            arr2 = arr[:]
            arr1.remove(max(arr))
            arr2.remove(min(arr))
            res = 1 + min(
                dfs(arr1),
                dfs(arr2)
            )
            cache[tuple(arr)] = res
            return res

    return dfs(arr)

        
