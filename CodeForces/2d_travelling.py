t = int(input())
for i in range(t):
    n, k, a, b = map(int, input().split())
    
    major = []
    source = [0, 0]
    dest = [0, 0]
    cities = []
    for j in range(n):
        
        x, y = map(int, input().split())
        
        if j < k:
            major.append((x, y))
        else:
            cities.append((x, y))
            
        if j == a - 1:
            source = [x, y]
            
        if j == b - 1:
            dest = [x, y]
            
        
        