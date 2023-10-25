n = int(input())


bills = [1, 5, 10, 20, 100]
length = 5


dp = [[float('inf') for i in range(n + 1)] for j in range(length)]

for i in range(length):
    dp[i][0] = 0
    
    
for i in range(length):
    for j in range(n + 1):
        if bills[i] <= j:
            dp[i][j] = min (dp[i][j], 1 + dp[i - 1][j - bills[i]])

min_bills = float('inf')
for i in range(length):
    min_bills = min(min_bills, dp[i][n])
    
print(min_bills)