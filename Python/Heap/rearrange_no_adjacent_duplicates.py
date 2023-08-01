from os import *
from sys import *
from collections import *
from math import *
import heapq
def rearrangeArray(arr,  n):

    # Write your code
    
    #RESULT ARRAY
    result = []

    #STORE ELEMENT AND FREQUENCY
    pq = []

    #ITERATE
    arr = sorted(arr)
    count = 1
    prev = arr[0]
    for i in range(1, len(arr)):
        if arr[i] == prev:
            count += 1

        else:
            heapq.heappush(pq, (-count, prev))
            count = 1
            prev = arr[i]

    heapq.heappush(pq, (-count, prev))


    #ALL FREQUENCIES STORED
    prev, freq = 0, 0
    while pq:
        #POP THE ELEMENT
        count, ele = heapq.heappop(pq)
        count = -count
        #ADD TO RESULT ARRAY
        result.append(ele)
        #ADD PREVIOUS ELEMENT TO QUEUE
        if freq!=0:
            heapq.heappush(pq, (-freq, prev))
        #STORE AS PREVIOUS WITH DECREMENETED FREQ
        prev = ele
        freq = count - 1

    return result
        
        


        

