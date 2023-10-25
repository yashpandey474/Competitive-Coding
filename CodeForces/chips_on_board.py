t = int(input())
a, b, n, min_row, min_col = 0, 0, 0, [], []

for m in range(t):
    n = int(input())

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    min_row = [float('inf') for k in range(n)]
    min_col = [float('inf') for p in range(n)]

    for i in range(n):
        for j in range(n):
            min_row[i] = min(min_row[i], a[i] + b[j])
            min_col[j] = min(min_col[j], a[i] + b[j])
            
    dp = [[0 for i in range(n)] for i in range(n)]
    
    dp[n - 1][n - 1] = min(min_row[n - 1], min_col[n - 1])
    for i in range(n - 1):
        dp[i][n - 1] = min(min_row[i], min_col[n - 1])
        dp[n - 1][i] = min(min_row[n - 1], min_col[i])
        
    for i in range(n - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            dp[i][j] = min(
                dp[i][j + 1] + min_col[j],
                dp[i + 1][j] + min_row[i]
            )
            
            
    print(dp[0][0])

