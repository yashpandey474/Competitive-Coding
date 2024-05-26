class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        total = sum(piles)
        n = len(piles)

        l = ceil(total / h)
        r = max(piles)


        def valid(mid):
            hours = 0

            for a in piles:
                hours += ceil(a/mid)
            
            return hours <= h

        sol = r

        while l <= r:
            mid = l + (r-l)//2

            if valid(mid):
                sol = mid
                r = mid - 1

            else:
                l = mid + 1

        return sol