from os import *
from sys import *
from collections import *
from math import *


def merge(arr1, start1, end1, arr2, start2, end2):
    i = start1
    j = start2
    arr3 = []
    inversions = 0

    while i<=end1 and j<=end2:
        if arr1[i]<=arr2[j]:
            arr3.append(arr1[i])
            i+=1
        else:
            inversions += end1 - i + 1
            arr3.append(arr2[j])
            j+=1

    arr3.extend(arr1[i:end1+1])
    arr3.extend(arr2[j:end2+1])
    arr1[start1:end2+1] = arr3[:]
    
    return inversions

    
def mergeSort(arr, start, end):
    if start < end:
        mid = (start+end)//2
        invL = mergeSort(arr, start, mid)
        invR = mergeSort(arr, mid+1, end)
        inv = merge(arr, start, mid, arr,  mid+1, end)
        
        return inv + invL + invR

    return 0

def getInversions(arr, n) :
	# Write your code here.
    return mergeSort(arr, 0, n-1)
    

# Taking inpit using fast I/O.
def takeInput() :
    n = int(input())
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n

# Main.
arr, n = takeInput()
print(getInversions(arr, n))
