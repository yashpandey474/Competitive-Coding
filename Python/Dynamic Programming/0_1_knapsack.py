#User function Template for python3

class Solution:
    
    def recursion(self, max_weight, current_value, val, wt, current_index):
        if current_index == len(val):
            return
        self.max_value = max(self.max_value, current_value)
        
        if max_weight - wt[current_index] >= 0:
            self.recursion(max_weight - wt[current_index], current_value + val[current_index],
            val,
            wt,
            current_index + 1
            )
        self.recursion(max_weight, current_value,
            val,
            wt,
            current_index + 1
        )
            
        
        
        
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
       
        # code here
        self.max_value = 0
        self.recursion(W, 0, val, wt, 0)
        return self.max_value
