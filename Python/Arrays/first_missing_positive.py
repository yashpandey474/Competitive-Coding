class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        #ITERATE THROUGH ARRAY
        n = len(nums)
        for i in range(n):
            #IF NUMBER IS NOT NEGATIVE AND IN RANGE
            while nums[i]>=1 and nums[i]<=n and nums[nums[i]-1] != nums[i]:
                #EXCHANGE IF NOT ALREADY PRESENT THERE
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]

        #ITERATE THROUGH ARRAY
        print(nums)
        for i in range(n):
            if nums[i] != i+1:
                return i+1

        return n+1

