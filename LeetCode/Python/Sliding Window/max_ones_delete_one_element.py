class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        i = 0
        j = 0
        zeroes = 0
        result = 0
        n = len(nums)

        while j<n:
            if nums[j] == 0:
                zeroes += 1
            while zeroes > 1:
                if nums[i] == 0:
                    zeroes -= 1
                
                i += 1
                
            result = max(result, j-i+1-zeroes)
            j+=1
        if result == n:
            return result-1
        return result
