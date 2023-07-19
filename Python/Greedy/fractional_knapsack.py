#User function Template for python3
'''
SIMPLE IMPLEMENTATION:
1. SORT THE ITEMS ON THEIR VALUE/WEIGHT
2. ITERATE FROM HIGHEST VALUE/WEIGHT
3. IF CURRENT HAS HIGHER WEIGHT; CHOOSE THE MAXIMUM VALUE WE CAN FROM IT BY REDUCING REMAINING WEIGHT TO 0
'''
class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w
        
class Solution:    
    #Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, W,arr,n):
        
        #  CREATE ARRAY SORTED ON VALUE/WEIGHT
        arr = sorted(arr, key = lambda x: x.value/x.weight, reverse = True)
        
        # ITERATE FROM HEIGHEST VALUE/WEIGHT TO LOWEST VALUE/WEIGHT
        current_weight = W
        current_value = 0
        for i in range(n):
            #CAN BE ADDED TO BAG AS WHOLE
            if current_weight - arr[i].weight >= 0:
                current_value += arr[i].value
                current_weight -= arr[i].weight
            #CANNOT BE ADDED OR ADDED AS FRACTION
            else:
                current_value += (arr[i].value/arr[i].weight) * current_weight
                current_weight = 0
                break
                
        return current_value
                
                
