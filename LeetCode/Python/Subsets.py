class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        subsets = []

        # FOR ALL BINARY STRINGS OF MAXIMUM N BITS
        for string in range(2**n):
            subset = []
            for i in range(n):
                # print(1 << i)
                if string & (1 << i):
                    subset.append(nums[i])

            subsets.append(subset)

        return subsets