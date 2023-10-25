class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #SLIDING WINDOW AND 2 POINTERS
        i = 0
        j = 0
        current_sum = nums[0]
        min_len = float('inf')

        while(j<len(nums)):
            if(current_sum < target):
                j += 1
                if j < len(nums):
                    current_sum += nums[j]
            elif (current_sum >= target):
                min_len = min(min_len, j-i+1)
                current_sum -= nums[i] 
                i+=1 #MOVE WINDOW FORWARD
        if min_len == float('inf'):
            return 0

        else:
            return int(min_len)
