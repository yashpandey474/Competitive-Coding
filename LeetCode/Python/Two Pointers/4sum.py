class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)
        sols = set()

        def three(start, target, prev, sols):
            for i in range(start, n - 2):
                reqdsum = target - nums[i]
                j = i + 1
                k = n - 1
                while j < k:
                    currsum = nums[j] + nums[k]

                    if currsum == reqdsum:
                        sols.add((prev, nums[i], nums[j], nums[k]))
                        j += 1
                        k -= 1

                    elif currsum < reqdsum:
                        j += 1

                    else:
                        k -= 1

            return

        for m in range(n - 3):
            reqdsum = target - nums[m]

            three(m + 1, reqdsum, nums[m], sols)


        return sols

            
                