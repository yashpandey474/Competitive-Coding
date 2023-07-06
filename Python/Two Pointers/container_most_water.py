class Solution:
    def maxArea(self, height: List[int]) -> int:
        current_ans = 0
        max_ans = 0

        i = 0
        j = len(height)-1

        while(i<=j):
            current_ans = (j-i)*min(height[i], height[j])
            max_ans = max(current_ans, max_ans)

            if(height[i]>height[j]):
                j-=1
            else:
                i+=1

        return max_ans
