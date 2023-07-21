from sys import stdin
import sys




def cutRod(price, n):

    # Write your code here.
    
    #DYNAMIC PROGRAMMING

    #CREATE THE DP ARRAY:: DP[I] = MAX PRICE OF SIZE I
    dp = [0]*(n+1)

    #ITERATE FOR ALL SIZES
    for i in range(1, n+1):

        #ITERATE FOR ALL SMALLER SIZES
        for j in range(0, i):

            #EITHER CUT BY J OR DON'T
            dp[i] = max(dp[i], price[j] + dp[i-j-1])

    return dp[n]




    










# Taking input using fast I/O.
def takeInput():
    n = int(input())

    price = list(map(int, input().strip().split(" ")))

    return price, n


# Main.
t = int(input())
while t:
    price, n = takeInput()
    print(cutRod(price, n))
    t = t-1
