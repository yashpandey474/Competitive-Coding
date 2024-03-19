t = int(input())

for test in range(t):
    n = int(input())
    c = list(map(int, input().split()))
    
    base = pow(2, 30)    
    count = set()
    mask = 0x7FFFFFFF
    matched = set()
    greater = 0
    
    for ele in c:
        if ele >= pow(2, 30):
            greater += 1
            
    for i in range(n):
        for j in range(n):
            
            if j in matched:
                continue
            
            a = c[i]
            b = c[j]
            result = (a & b) | (~a & ~b) & mask
            if a >= base and b < base and result == 0:
                matched.add(j)
    
    lesser = n - greater
    match = len(matched)
    
    # print(lesser, greater, match)
    print(lesser + greater - match)                
    
