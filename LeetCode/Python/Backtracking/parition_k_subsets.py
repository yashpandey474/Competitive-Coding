class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total_sum = sum(nums)

        #CANNOT BE DIVIDED
        if total_sum % k:
            return False
        #IMPROV EFFICIENCY
        nums = sorted(nums, reverse = True)
        target = total_sum / k
        
        #BUILD K SUBSETS WITH THIS TARGET SUM

        #KEEP TRACK OF USED ELEMENTS
        used = [False]*len(nums)


        #IMPLEMENT BACKTRACKING
        def backtrack(index, k, currentSum):
            if k == 0:
                return True

            if currentSum == target:
                return backtrack(0, k-1, 0)

            else:
                #FIND A SUBSET WITH THAT TARGET SUM
                for j in range(index, len(nums)):
                    if used[j] or  currentSum + nums[j] > target:
                        continue

                    used[j] = True

                    if (backtrack(j + 1, k, currentSum + nums[j])):
                        return True
                    used[j] = False

                return False

        return backtrack(0, k, 0)



    
