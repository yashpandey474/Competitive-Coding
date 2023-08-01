class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def canLoad(max_weight):
            #GREEDY PROBLEM
            curDays = 1
            curWeight = 0
            for w in weights:
                if curWeight + w > max_weight:
                    curDays += 1
                    curWeight = w

                else:
                    curWeight += w

            return curDays <= days
        #LOWEST POSSIBLE
        left = max(weights)
        #WORST POSSIBLE
        right = sum(weights)
        #CURRENT BEST IN WORST CASE
        result = right

        #BINARY SEARCH
        while left<=right:
            mid = (left + right)//2

            #CHECK IF VALID
            if canLoad(mid):
                #UPDATE WORST POSSIBLE
                right = mid - 1
                result = mid

            else:
                #UPDATE LOWEST POSSIBLE
                left = mid + 1

        return result
