t = int(input())


import heapq

for i in range(t):
    n, c = map(int, input().split())
    arr = list(map(int, input().split()))
    
    heap = []
    
    for j in range(n):
        heapq.heappush(heap, j + 1 + arr[j])
        
    total = 0
    while heap and c > 0:
        curr = heapq.heappop(heap)
        
        if c - curr >= 0:
            total += 1
            c -= curr
            
        else:
            break
        
    print(total)
        
    