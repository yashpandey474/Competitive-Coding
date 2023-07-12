class Solution:
    def countOnes(self, n):
        count = 0
        while n:
            n = n & n-1
            count += 1
        return count
    def countBits(self, n: int) -> List[int]:
        output = []
        for i in range(0, n+1):
            output.append(self.countOnes(i))
        return output
