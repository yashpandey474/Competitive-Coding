n = int(input())

arr = list(map(int, input().split()))

max_integer = max(arr)

dp = [0]*(max_integer + 1)

freq = {i: 0 for i in arr}
for i in arr:
    freq[i] += 1
    

    
for i in range(max_integer + 1):
    if i not in freq:
        dp[i] = max(dp[i - 1], dp[i - 2])
        continue
    dp[i] = max(
        dp[i - 1], dp[i - 2] + freq[i]*i
    )
    
# print("DP = ", dp)
# print("FREQ = ", freq)
print(dp[max_integer])