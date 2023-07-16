class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        power_set = set()
        nums = sorted(nums)
        for i in range(0, pow(2,n)):
            subset = []
            for j in range(0, n):

                if ((i >> j) & 1):
                    subset.append(nums[j])
            
            power_set.add(tuple(subset))

        return list(power_set)
