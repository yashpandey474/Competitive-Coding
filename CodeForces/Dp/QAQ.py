string = input()

n = len(string)


dp = [0 for i in range(n)]

for i in range(n):
    for j in range(i):
        
        if string[i] == "A" and string[j] == "Q":
            dp[i] += 1
            
        if string[i] == "Q" and string[j] == "A":
            dp[i] += dp[j]
            
            
total = 0
for i in range(n):
    if string[i] == "Q":
        total += dp[i]

print(total)