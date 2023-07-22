class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:

        #SORT THE ARRAY
        nums = sorted(nums)

        #ITERATE WITH TWO POINTERS
        left, right = 0, 0
        result, total = 0, 0

        while right < len(nums):
            total += nums[right]

            while nums[right]*(right - left + 1) > total + k:
                total -= nums[left]
                left+=1

            result = max(result, right - left + 1)
            right += 1

        return result


            
