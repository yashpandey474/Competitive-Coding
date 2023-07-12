class Solution:
    def recursion(self, n: int, k: int, answer):
        if k == 0:
            self.res.append(answer)
            return
        if len(answer) == 0:
            j = 0
        else:
            j = answer[-1]
        for i in range(j+1, n+1):
            self.recursion(n, k-1, answer + [i])
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.res = []
        self.recursion(n, k, [])
        return self.res
