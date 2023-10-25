#Your task is to complete this function
#Your should return the required output
class Solution:
    def maxLen(self, n, arr):
        map_sums = {}
        current_sum = 0
        max_len = 0
        
        for i in range(n):
            current_sum += arr[i]
            
            if current_sum == 0:
                max_len = max(max_len, i+1)
            
            if current_sum in map_sums:
                length = i - map_sums[current_sum]
                max_len = max(max_len, length)
            
            else:
                map_sums[current_sum] = i
        
        return max_len
