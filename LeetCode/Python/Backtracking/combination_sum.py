class Solution(object):

    def recursion(self, candidates, target, answer, current_sum):
        if current_sum == target:
            actual = tuple(sorted(answer))
            if actual not in self.set:
                self.set.add(actual)
                self.res.append(answer)
            return

        if current_sum > target:
            return
        for i in candidates:
            self.recursion(candidates, target, answer + [i], current_sum + i)
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.res = []
        self.set = set()
        self.recursion(candidates, target, [], 0)

        return (self.res)
