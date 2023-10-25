from typing import List

def bubbleSort(arr: List[int], n: int):
    # Your code goes here.
    
    i = n-1

    #ITERATE FROM LAST INDEX
    while i>0:
        #ITERATE FROM START TO CURRENT
        for j in range(0, i):
            #BRING REMAINING MAX ELEMENT TO ITH INDEX
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            
        i-=1
    
    return 
