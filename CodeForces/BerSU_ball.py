n1 = int(input())
arr1 = sorted(list(map(int, input().split())))
n2 = int(input())
arr2 = sorted(list(map(int, input().split())))



dp = [[0 for i in range(n2)] for i in range(n1)]
for i in range(n1):
    for j in range(n2):
        if i > 0  and j > 0:
            dp[i][j] = max(dp[i][j], dp[i - 1][j- 1])
        
        if abs(arr1[i] - arr2[j]) <= 1:
            dp[i][j] += 1
            
        if i > 0:
            dp[i][j] = max(dp[i][j], dp[i - 1][j])
            
        if j > 0:
            dp[i][j] = max(dp[i][j], dp[i][j - 1])
        
        

max_val = 0
for i in range(n1):
    max_val = max(max_val, max(dp[i]))
print(max_val)
    