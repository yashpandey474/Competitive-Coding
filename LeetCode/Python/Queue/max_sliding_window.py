class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        #CREATE AN ARRAY TO STORE VALUES
        n = len(nums)
        values = []
        
        #DEQUE TO STORE ELEMENTS SEEN SO FAR
        deque = [] #INDICES

        start = end = 0

        while end<n:
            #POP PREVIOUS LESSER ELEMENTS
            while deque and nums[deque[-1]] < nums[end]:
                deque.pop()

            #ADD NEW ELEMENT TO RIGHT
            deque.append(end)
            
            #IF LEFT INDEX IS OUT OF BOUNDS
            if start > deque[0]:
                deque.pop(0)
            #MOVE WINDOW
            
            if end + 1 >= k:
                values.append(nums[deque[0]])
                start+=1

            end+=1

        return values
