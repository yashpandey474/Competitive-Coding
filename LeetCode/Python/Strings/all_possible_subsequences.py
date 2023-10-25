#User function Template for python3

class Solution:
            
	def AllPossibleStrings(self, s):
		# Code here
		n = len(s)
		res = []
		for i in range(0, pow(2, n)):
		    sub = ""
		    for j in range(0, n):
		        
		        if i & (1 << j):
		            sub += s[j]
		    if sub != "":       
		        res.append(sub)
		    
		return sorted(res)
		
