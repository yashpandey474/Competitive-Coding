t = int(input())
n, k, x = 0, 0, 0

for i in range(t):
    n, k, x = map(int, input().split())
    
    
    #MINIMUM SUM POSSIBLE & MAXIMUM SUM POSSIBLE
    total_sum = n*(n + 1)//2
    first_n_k = (n - k)*(n - k + 1)//2
    min_sum = k*(k + 1)//2
    max_sum = total_sum - first_n_k
        
        
    res = (min_sum <= x <= max_sum)
    
    print("YES" if res else "NO")
            
    