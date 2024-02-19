dp = [0 for i in range(2*(10**5) + 1)]

for c in range(1, 2*(10**5) + 1):
    curr_sum = 0
    i = c
    while i:
        curr_sum += (i%10)
        i = i//10
        
    dp[c] = dp[c - 1] + curr_sum
    
for test in range(int(input())):
    n = int(input())
    
    print(dp[n])
        
           
        
        