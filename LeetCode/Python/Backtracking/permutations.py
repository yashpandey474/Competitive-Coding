class Solution:
    def recursion(self, nums, answer,used):
        if len(nums) == len(answer):
            self.res.append(answer)
            return
        
        else:
            for i in nums:
                if i not in used or used[i] == False:
                    used[i] = True
                    self.recursion(nums, answer + [i], used)
                    used[i] = False

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        if not nums:
            return self.res
        self.recursion(nums, [], {})
        return self.res
