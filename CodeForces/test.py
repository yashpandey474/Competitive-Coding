from math import gcd
t = int(input())

for i in range(t):
    l, r = map(int, input().split())
    found = False
    for i in range(1, r):
        for j in range(1, r):
            if i == j:
                continue
            
            if gcd(i, j) != 1 and l<=i + j <=r:
                print(i, j)
                found = True
                break
            
        if found:
            break
        
    if not found:
        print(-1)
                