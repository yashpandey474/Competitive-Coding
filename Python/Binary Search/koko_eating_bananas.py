class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def canEat(mid):
            hours = 0
            for p in piles:
                hours += ceil(p/mid)
            
            return hours <= h
                
        #LOWEST POSSIBLE
        left = 1
        #WORST POSSIBLE
        high = max(piles)
        #BEST IN WORST CASE
        result = high

        while left <= high:
            mid = (left + ((high - left)//2))

            if canEat(mid):
                result = mid
                #UPDATE HIGHEST
                high = mid - 1

            else:
                #UPDATE LOWEST
                left = mid + 1

        return result
