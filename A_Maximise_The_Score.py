t = int(input())

for test in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    a = sorted(a, reverse = True)
    
    count = 0
    for i in range(1, 2*n, 2):
        count += a[i]
        
    print(count)