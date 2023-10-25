class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        #TWO-POINTER APPROACH
        i = 0
        j = len(height)-1
        leftMax = 0
        rightMax = 0
        total_water = 0

        while i <= j:
            if height[i] <= height[j]:

                if height[i] >= leftMax:
                    leftMax = height[i]
                elif height[i] < leftMax:
                    total_water += leftMax - height[i]

                i+=1

            else:
                
                if height[j] >= rightMax:
                    rightMax = height[j]

                elif height[j] < rightMax:
                    total_water += rightMax - height[j]

                j-=1
        
        return total_water
