t = int(input())

def binSearch(num, arr, prefix):
    st = 0
    
    n = len(arr)
    en = n - 1
    result = -1
    
    while st <= en:
        mid = (en + st)//2
        
        if arr[mid] <= num:
            st = mid + 1
            result = mid
        
        else:
            en = mid - 1
    
    # print("RES: ", result)
    
    if result == -1:
        return 0
    
    return prefix[result]
        
for i in range(t):
    n, q = map(int, input().split())
    
    heights = list(map(int, input().split()))
    heightmax = heights[:]
    
    maxno = heights[0]
    for index, m in enumerate(heights):
        maxno = max(maxno, heights[index])
        heightmax[index] = maxno
        
    numbers = list(map(int, input().split()))
    
    prefix = [0]*n
    
    prefix[0] = heights[0]
    # print("HI:", heights)
    for index in range(1, n):
        prefix[index] = heights[index] + prefix[index - 1] 

    # print("PRE:", prefix)
    for num in numbers:
        print(binSearch(num, heightmax, prefix), end= " ")
        
    print()
        