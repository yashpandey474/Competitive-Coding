class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total = 0
        n = len(nums)
        for string in range(2**n):
            xor = 0
            for j in range(n):
                if string & (1 << j):
                    xor ^= nums[j]

            total += xor

        return total
