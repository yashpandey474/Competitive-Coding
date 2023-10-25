class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for index, num in enumerate(nums):
            nums[index] = str(num)

        def compare(n1, n2):

            if n1 + n2 > n2 + n1:
                #N1 FIRST
                return - 1
            else:
                #N2 FIRST
                return 1

        nums = sorted(nums, key = cmp_to_key(compare))

        result = "".join(nums)

        return str(int(result))
