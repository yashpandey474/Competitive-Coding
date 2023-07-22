class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        #ITERATE ONCE THROUGH THE ARRAY

        #MAX
        maxArea = 0
        #STACK
        stack = [] #PAIR = (INDEX, HEIGHT)

        for i, h in enumerate(heights):
            #SET START INDEX
            start = i
            #POP GREATER HEIGHTS FROM STACK
            while stack and stack[-1][1] > h:
                #POP
                index, height = stack.pop()
                print("I = ", i, "INDEX = ", index, "HEIGHT = ", height)
                #CHECK FOR MAX AREA
                maxArea = max(maxArea, height * (i - index))
                #UPDATE START OF CURRENT
                start = index

            #ADD TO STACK
            stack.append((start, h))

        #SEE REMAINING ELEMENTS
        for i, height in stack:
            maxArea = max(maxArea, height * (len(heights) - i))


        #RETURN MAX AREA
        return maxArea
                
