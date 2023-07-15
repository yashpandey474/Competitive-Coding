class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        start = 0
        end = n-1
        

        while start < end:
            mid = (start+end)//2
            
            #EVEN
            if mid%2 == 0:
                #ON RIGHT SIDE
                if nums[mid] == nums[mid+1]:
                    start = mid+2
                else:
                    end = mid

            #ODD
            else:
                #ON RIGHT SIDE
                if nums[mid] == nums[mid-1]:
                    start = mid+1
                
                else:
                    end = mid-1
                
        return nums[start]
            
        
