t = int(input())
 
 
def maxK(traps):
    i = 1
    
    while i:
        found = False
        for j in traps:
            if j >= i:
                continue
            if j - 1 + traps[j] <=  (i - 1) + (i - j):
                found = True
                break
            
        if found:
            break
        i += 1
        
    return i - 1
 
for i in range(t):
    n = int(input())
    traps = {}
     
    for i in range(n):
        d, s = map(int, input().split())
        
        if d in traps:
            traps[d] = min(traps[d], s)
        else:
            traps[d] = s
        
    print(maxK(traps)) 