

def shift_array(arr: List[int], n: int) -> List[int]:
    #REVERSE ENTIRE ARRAY
    arr = arr[::-1]
    
    # REVERSE FIRST K ELEMENTS
    arr = arr[n-1::-1] + arr[len(arr)-1:n-1:-1]
    
    # REVERSE LAST N-K ELEMENTS
    
    return arr
    
