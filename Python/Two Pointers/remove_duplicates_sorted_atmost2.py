class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        start = 2
        end = 2
        n = len(nums)

        if(n<=2):
            return n

        while(end < n):
            if(nums[end] == nums[end-1] == nums[end-2]):
                end+=1
            else:
                nums[start] = nums[end]
                if(start== end-1 and end<n-1 and nums[end] == nums[end+1]):
                    end+=2
                    start += 2
                else:
                    end+=1
                    start+=1

        return start
