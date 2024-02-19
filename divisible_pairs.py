t = int(input())

for test in range(t):
    n, x, y = map(int, input().split())
    
    a = list(map(int, input().split()))
    
    count = 0
    
    map1 = {}
    
    for i in range(n):
        rem1 = a[i] % x
        rem2 = a[i] % y
        
        rem1a = x - rem1
        
        # print(a[i], rem1, rem2, rem1a)
        if rem1 == 0:
            rem1a = 0
            
        if (rem1a, rem2) in map1:
            count += map1[(rem1a, rem2)]
            
        if (rem1, rem2) not in map1:
            map1[(rem1, rem2)]  = 0
            
        map1[(rem1, rem2)]  += 1
        
    print(count)
        
        
        