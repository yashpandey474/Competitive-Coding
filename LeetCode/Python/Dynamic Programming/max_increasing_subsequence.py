#User function Template for python3
class Solution:
	def maxSumIS(self, Arr, n):
		# code here
        
        #USE DYNAMIC PROGRAMMING
        
        #INITIALISE DP ARRAY
        dp = [0 for _ in range(n)]
        #iNITIALISE VARIABLE TO STORE MAX SUM
        max_sum = 0
        
        #ITERATE THROUGH THE ARRAY
        for i in range(0, n):
            #GO BACKWARDS TO FIND CANDIDATE ELEMENTS
            for j in range(0, i):
                #CAN BE ADDED TO SUBSEQUENCE
                if Arr[j] < Arr[i]:
                    dp[i] = max(dp[i], dp[j])
                    
            dp[i] += Arr[i]
            max_sum = max(max_sum, dp[i])
                
        #RETURN THE MAX_SUM
        return max_sum
