class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        map_remainders = {0: -1}
        curr = 0

        for index, num in enumerate(nums):
            curr += num
            rem = curr % k

            if rem in map_remainders:
                if index - map_remainders[rem] >= 2:
                    return True

            else:
                map_remainders[rem] = index

        return False
