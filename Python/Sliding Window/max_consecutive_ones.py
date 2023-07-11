class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        #TWO POINTERS AND SLIDING WINDOW
        i = 0
        j = 0

        while j < len(nums):
            if nums[j] == 0:
                k-=1
            #EXHAUSTED 
            if k < 0:
                if(nums[i] == 0):
                    k += 1
                #MOVE WINDOW FORWARD
                i += 1
            
            j += 1
    
        return j - i
