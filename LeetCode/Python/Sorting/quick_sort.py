"""
	The function is called with the parameters:
	quickSort(input, 0, size - 1);

"""
from typing import List
import random
def partitionArr(arr, startIndex, endIndex):
    
    #GET THE PIVOT INDEX
    pivot = random.randint(startIndex, endIndex)
    pivEle = arr[pivot]
    #EXCHANGE PIVOT WITH FIRST ELEMENT
    arr[startIndex], arr[pivot] = arr[pivot], arr[startIndex]

    #USE TWO POINTERS
    low = startIndex
    high = endIndex
    while low<=high:
        while low <= endIndex and arr[low] <= pivEle:
            low+=1

        while arr[high] > pivEle:
            high -= 1

        if low < high:
            #SWAP THE ELEMENTS
            arr[low], arr[high] = arr[high], arr[low]

    #PLACE THE ELEMENT
    arr[startIndex], arr[high] = arr[high], arr[startIndex]
    return high



def quickSort(arr: List[int], startIndex: int, endIndex: int):
    """
    Don't write main().
    Don't read input, it is passed as function argument.
    Change in the given array itself.
    Taking input and printing output is handled automatically.
    """
    if startIndex < endIndex:
        #GET PARTITION INDEX
        partIndex = partitionArr(arr, startIndex, endIndex)

        #RECURSE ON BOTH HALVES
        quickSort(arr, startIndex, partIndex-1)
        quickSort(arr, partIndex+1, endIndex)
