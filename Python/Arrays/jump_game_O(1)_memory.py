class Solution:
    def canJump(self, nums: List[int]) -> bool:
        sum1 = 0
        i = 0
        while(i>=0):

            if(i >= len(nums)-1):
                return True

            if(nums[i] == 0):
                i-=1

            else:
                temp = i
                i = i+nums[i]
                nums[temp] = 0
    
        return False
