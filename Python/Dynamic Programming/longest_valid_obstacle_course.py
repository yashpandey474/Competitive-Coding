class Solution:
    def longestObstacleCourseAtEachPosition(self, nums: List[int]) -> List[int]:
        #I = LENGTH OF LIS, DP[I] IS SMALLEST ENDING VALUE
        dp = [10**8] * (len(nums) + 1)
        answer = []


        for num in nums:
            #FIND INDEX TO INSERT
            index = bisect.bisect(dp, num)
            answer.append(index + 1)
            dp[index] = num


        return answer

        

            
