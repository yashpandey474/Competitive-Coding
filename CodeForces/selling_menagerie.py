t = int(input())


def maxProfit(a, c, n):
    dp1 = [c[i] for i in range(n)]
    dp2 = [2*c[i] for i in range(n)]
    
    
    for i in range(n):
        dp1[i] = max(
            dp1[i] + dp1[a[i] - 1],
            dp2[i] + dp1[a[i] - 1]
        )
        
        dp2[i] = max(
            dp2[i] + dp1[a[i] - 1],
            dp2[i] + dp1[a[i] - 1]
        )
    
    return max(max(dp1), max(dp2))
            
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    c = list(map(int, input().split()))
    
    
    res = maxProfit(a, c, n)
    string = ""
    for i in res:
        string += str(i) + " "
        
    print(string.rstrip())