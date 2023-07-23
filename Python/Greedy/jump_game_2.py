class Solution:

            
    def jump(self, nums: List[int]) -> int:
        
        #NUMBER OF JUMPS
        jumps = 0
        #WINDOW WHERE JUMPS IS KNOWN
        l = r = 0

        #WHILE WINDOW DOESN'T COVER LAST
        while r<len(nums)-1:
            #FARTHEST INDEX WE CAN REACH FROM CURRENT WINDOW
            farthest = 0
            for i in range(l, r+1):
                #FIND FARTHEST FROM THE RANGE
                farthest = max(farthest, i + nums[i])
            #MOVE L TO 1 AFTER RIGHT
            l = r+1
            #MOVE RIGHT TO FARTHEST INDEX
            r = farthest
            #INCREASE NUMBER OF JUMPS
            jumps += 1

        #RETURN NUMBER OF JUMPS
        return jumps
