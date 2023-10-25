class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        #DP ARRAY: DP[I] = IF SUBSTRING S[0:I] CAN BE CONSTRUCTED USING WORDDICT
        dp = [False for _ in range(n+1)]

        #BASE CASE: EMPTY STRING
        dp[0] = True

        #ITERATE FOR ALL LENGTHS
        for i in range(1, n+1):
            #ITERATE FOR INDICES
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break

        return dp[n]


    

            

        
