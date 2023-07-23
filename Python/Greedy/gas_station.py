'''
1. APPROACH: KEEP A TOTAL VARIABLE FOR DIFFERENCE BETWEEN GAS AND COST
2. KEEP ADDING THE DIFFERENCES TO TOTAL
3. IF TOTAL IS LESS THAN 0 AT CURRENT: TRY NEXT AS START AND RESET TOTAL
4. RETURN THE INDEX WHERE TOTAL REMAINED  > 0  FOR REMAINING PART OF ARRAY
5. IF SUM OF GAS  < SUM OF COST A SOLUTION IS NOT POSSIBLE; ELSE A UNIQUE SOLUTION ALWAYS POSSIBLE
'''
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        #TWO POINTERS
        n = len(gas)

        #CREATE THE DIFF ARRAY
        diff = [gas[_] - cost[_] for _ in range(n)]
        print(diff)

        if sum(diff) < 0:
            return -1

        #SINCE SUM OF ARRAY IS 0 AND THERE EXISTS ONE UNIQUE AND SOLUTION
        #AS SOON AS ABLE TO REACH END: SOLUTION
        total = 0
        start = 0
        for i in range(n):
            total += diff[i]
            if total < 0:
                total = 0
                start = i+1
        return start
