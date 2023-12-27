n, a, b, c = map(int, input().split())

min_val = min([a, b, c])

dp = [-float('inf')] * (n + 1)

dp[0] = 0

for length in range(min_val, n + 1):
    if length - a >= 0:
        dp[length] = max(dp[length], dp[length - a] + 1)
        
    if length - b >= 0:
        dp[length] = max(dp[length], dp[length - b] + 1)
        
    if length - c >= 0:
        dp[length] = max(dp[length], dp[length - c] + 1)
    
        

print(dp[n])