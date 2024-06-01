class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 2:
            return nums

        total = 0
        for i in nums:
            total = total ^ i

        # FIND RIGHTMOST SET BIT
        rightmost = total & (-total)
        total1 = 0
        total2 = 0

        for i in nums:
            if rightmost & i:
                total1 = total1 ^ i
            else:
                total2 = total2 ^ i

        return [total1, total2]