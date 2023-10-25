t = int(input())

for m in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    q = int(input())
    

    for i in range(q):
        l, k = map(int, input().split())
        l -= 1
        
        #PREFIX AND ARRAY
        prefix_and = [arr[0]]
        for i in range(1, n):
            prefix_and.append(prefix_and[-1] & arr[i])
            
        #FIND MAXIMAL RR
        left = l
        right = n - 1
        res = -1
        
        while left <= right:
            mid = left + (right - left)//2
            
            if prefix_and[mid] >= k:
                res = mid
                left = mid + 1
                
            else:
                right = mid - 1
        
        print(res + 1, end = " ")    
    print()
            