def pushZerosAtEnd(arr):
    # write your code here
    nonZero = 0
    n = len(arr)

    for i in range(n):
        if arr[i] != 0:
            arr[i], arr[nonZero] = arr[nonZero], arr[i]
            nonZero += 1
            
    return arr
