t = int(input())

for i in range(t):
    n = int(input())
    candies = list(map(int, input().split()))
    
    total = sum(candies)
    
    if total % 2 != 0:
        print("NO")
        continue
    
    dp = [[False for i in range(total//2 + 1)] for i in range(n)]
    
    
    for i in range(n):
        dp[i][0] = True
        
    for i in range(n):
        for j in range(1, total//2 + 1):
            dp[i][j] = dp[i - 1][j]
            
            if j >= candies[i]:
                dp[i][j] = dp[i][j] or dp[i][j - candies[i]]
                
    if dp[n - 1][total//2]:
        print("YES")
        continue
    
    print("NO")
        
    