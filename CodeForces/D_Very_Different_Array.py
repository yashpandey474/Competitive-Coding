t = int(input())
            
            
for t1 in range(t):
    cache = {}
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    b = sorted(b, reverse = True)
    a = sorted(a)
    
    
    curr_prefix = 0
    lis2 = b[-n:]
    d = sum([a[i] - lis2[i] for i in range(n)])
    
    print(lis2)
    max_diff = d
    for i in range(1, n):
        d  -= a[i] - b[(m - n - i - 1)]
        d += a[i] - b[i]
        max_dff = max(max_diff, d)
        
    print(max_diff)        
        