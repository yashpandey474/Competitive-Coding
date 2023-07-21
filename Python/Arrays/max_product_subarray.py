#User function Template for python3
class Solution:

	# Function to find maximum
	# product subarray
	def maxProduct(self,arr, n):
		# code here
		if not arr:
		    return 0
		i = 1
		maxProd = arr[0]
		currMaxProd = arr[0]
		currMinProd =arr[0]
		
		while i < len(arr):
		    
		    #EXCHANGE MAX AND MIN IF LESS THAN 0
		    if arr[i] < 0:
		        currMaxProd, currMinProd = currMinProd, currMaxProd
		        
		    currMaxProd = max(arr[i], arr[i]*currMaxProd)
		    maxProd = max(currMaxProd, maxProd)
		    currMinProd = min(currMinProd*arr[i], arr[i])
		    i+=1
		    
		return maxProd
		    
