t = int(input())
for i in range(t):
    l = list(map(int, input().split()))
    
    if len(set(l)) == 1:
        print(1, 1, 1)
        continue
    elif len(set(l)) == 3:
        m = max(l)
    
    else:
        m = l[0] ^ l[1] ^ l[2]
        
    if l[0] == m:
        print(1, 0, 0)
            
    elif l[1] == m:
        print(0, 1, 0)
            
    else:
        print(0, 0, 1)
        
        
        
        
        