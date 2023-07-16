class Solution(object):

    def recursion(self, candidates, target, answer, current_sum, current_index):
        if current_sum == target:
            self.res.add(tuple((answer)))
            return

        if current_sum > target:
            return
        
        for i in range(current_index, len(candidates)):
            #SKIP DUPLICATES
            if i>current_index and candidates[i] == candidates[i-1]:
                continue
            self.recursion(candidates, target, answer + [candidates[i]], current_sum + candidates[i], i+1)
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.res = set()
        candidates = sorted(candidates)
        self.recursion(candidates, target, [], 0, 0)

        return list(self.res)
