#User function Template for python3
class Solution:
    
    def recursion(self, arr, current_sum, current_index):
        if current_index >= len(arr):
            return
        
        #TAKE
        self.result.append(current_sum+arr[current_index])
        self.recursion(arr, current_sum + arr[current_index], current_index+1)
        
        #NOT TAKE
        self.recursion(arr, current_sum, current_index+1)
    
	def subsetSums(self, arr, N):
		# code here
        self.result = [0]
        self.recursion(arr, 0, 0)
        
        return self.result
