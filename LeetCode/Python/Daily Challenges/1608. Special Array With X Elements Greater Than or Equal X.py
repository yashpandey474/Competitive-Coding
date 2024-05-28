class Solution:
    def specialArray(self, nums: List[int]) -> int:
        count = [0]*(1001)

        for i in nums:
            count[i] += 1

        total = 0
        for i in range(1000, -1, -1):
            total += count[i]

            if total == i:
                return i

        return -1