class Solution(object):

    def recursion(self, nums, answer, used, start):
        self.res.append(answer)
        if len(nums) == len(answer):
            return

        while start < len(nums):
            if nums[start] not in used or used[nums[start]] == False:
                used[nums[start]] = True
                self.recursion(nums, answer + [nums[start]], used, start+1)
                used[nums[start]] = False
            start+=1
        
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        self.res = []
        used = {}
        self.recursion(nums, [], used, 0)
        return self.res
