t = int(input())
heights = []
n, x = 0, 0

def canFill(height):
    total = 0
    for h in heights:
        if h >= height:
            continue
        
        total += height - h
        
    return total <= x

for i in range(t):
    n, x = map(int, input().split())
    
    heights = list(map(int, input().split()))
    
    l = min(heights)
    r = min(heights) + x
    
    if n == 1:
        print(heights[0] + x)
        continue
    
    res = l
    while l <= r:
        mid = l + (r - l)//2
        
        if canFill(mid):
            res = mid
            l = mid + 1
            
            
        else:
            r = mid - 1
            
            
    print(res)