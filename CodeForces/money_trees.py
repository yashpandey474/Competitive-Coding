t = int(input())
n, k, heights, fruits, prefix, length = 0, 0, [], [], [], []


def get(dist):
    found = False
    
    for i in range(n - dist + 1):
        if length[i] < dist:
            continue
        
        _sum = prefix[i + dist] - prefix[i]
        
        if _sum <= k:
            found = True
            break
        
        
    return found

for i in range(t):
    n, k = map(int, input().split())
    
    fruits = list(map(int, input().split()))
    heights = list(map(int, input().split()))
    
    #PREFIX SUM
    prefix = [0 for i in range(n + 1)]
    
    for i in range(0, n):
        prefix[i + 1] = prefix[i] + fruits[i]
        
    #LENGTH WHERE DIVISIBILITY HOLDS
    length = [1 for i in range(n)]
    
    for i in range(n - 2, -1, -1):
        if heights[i]%heights[i + 1] == 0:
            length[i] = length[i + 1] + 1
            
    #TWO POINTERS
    l = 0
    r = n
    
    while l <= r:
        mid = l + (r - l)//2
        
        if get(mid):
            l = mid + 1
            
        else:
            r = mid - 1
            
    print(r)
    
    
            
    