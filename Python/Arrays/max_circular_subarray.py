class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #CASE 1 - MAXIMUM SUBARRAY SUM
        #CASE 2 - CIRCULAR MAXIMUM SUBARRAY SUM: SUBTRACT MIN SUBARRAY SUM FROM TOTAL SUM

        total_sum = 0
        current_sum_max = 0
        current_sum_min = 0
        max_sum = nums[0]
        min_sum = nums[0]

        for i in nums:
            total_sum += i

            current_sum_max = max(i, current_sum_max+i)
            current_sum_min = min(i, current_sum_min+i)

            max_sum = max(max_sum, current_sum_max)
            min_sum = min(min_sum, current_sum_min)
        if(total_sum == min_sum): #ALL ELEMENTS ARE NEGATIVE
            return max_sum
        return max(max_sum, total_sum-min_sum)


