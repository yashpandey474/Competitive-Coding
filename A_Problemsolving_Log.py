t = int(input())

for i in range(t):
    n = int(input())
    s = str(input())
    
    m = {}
    for j in range(ord("A"), ord("Z") + 1):
        if chr(j) not in m:
            m[chr(j)] =  j - ord("A") + 1
            
    total = 0
    for a in s:
        # print("a = ", a)
        if m[a] == 0:
            continue
        
        m[a] -= 1
        if m[a] == 0:
            total += 1
            
            
    # print("S = ", s, "M = ", m)
    print(total)
    
    
