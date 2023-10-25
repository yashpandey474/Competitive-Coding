from os import *
from sys import *
from collections import *
from math import *

def insertHeap(heap, element):
    index = 0
    while index < len(heap) and heap[index] < element:
        index += 1
    heap.insert(index, element)

def popHeap(heap):
    return heap.pop(0)

def minHeap(N: int, Q: [[]]) -> []:

    # Write your code frome here.
    heap = []
    result = []
    n = len(Q)
    for i in Q:
        if i[0] == 1:
            result.append(popHeap(heap))

        else:
            insertHeap(heap, i[1])
    return result


