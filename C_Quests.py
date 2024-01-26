import heapq

t = int(input())

for test in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    total_xp = 0
    max_sum = 0
    res = 0
    # CURRENT MAX COMPLETED
    for i in range(min(n, k)):
        total_xp += a[i]
        max_sum = max(max_sum, b[i])
        res = max(res, total_xp + max_sum * (k - i - 1))
        
    print(res)