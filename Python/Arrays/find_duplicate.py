class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if len(nums) == 0:
            return -1
        #TWO POINTERS; USE HARE-TORTOISE ALGORITHM
        slow = nums[0]
        fast = nums[nums[0]]
        
        #MAKE POINTERS MEET
        while (slow != fast):
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        #ANOTHER POINTER FROM START OF ARRAY
        fast = 0
        while fast != slow:
            fast = nums[fast]
            slow = nums[slow]
        
        return slow
