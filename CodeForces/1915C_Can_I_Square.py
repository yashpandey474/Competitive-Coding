import math


t = int(input())

for i in range(t):
    n = int(input())
    
    a = list(map(int, input().split()))
    
    total = sum(a)
    
    if math.sqrt(total).is_integer():
        print("YES")
        
    else:
        print("NO")
        
    