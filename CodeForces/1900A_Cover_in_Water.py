t = int(input())

import math


for i in range(t):
    n = int(input())
    s = str(input())
    
    s = "#" + s + "#"
    hashes = []
    
    for j in range(len(s)):
        if s[j] == "#":
            hashes.append(j)
        
    res1 = 0    
    for j in range(len(hashes) - 1):
        a = hashes[j]
        b = hashes[j + 1]
        
        if (b - a - 1) >= 3:
            res1 = 2
            break
        
        else:
            res1 += (b - a - 1)
        
    print(res1)
        
        
        
    