class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums)-1
        
        while start <= end:
            mid = (start+end)//2

            if mid<len(nums)-1 and nums[mid] > nums[mid+1]:
                return nums[mid+1]
            
            if mid>0 and nums[mid] < nums[mid-1]:
                return nums[mid]
            
            if nums[mid] > nums[end]:
                start = mid+1
            
            else:
                end = mid-1

        return nums[mid]
