class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:

        cache = {}
        n = len(stoneValue)

        def dfs(index, turn):
            
            #OUT OF BOUNDS
            if index >= n:
                return 0

            #ALREADY CACHED
            if (index, turn) in cache:
                return cache[(index, turn)]

            #CALCULATE
            if turn:
                res = -float('inf')
                current = 0
                for i in range(index, min(n, index + 3)):
                    current += stoneValue[i]
                    res = max(
                        res,
                        current + dfs(i + 1, False)
                    )

            else:
                res = float('inf')
                current = 0
                for i in range(index, min(n, index + 3)):
                    current += stoneValue[i]
                    res = min(
                        res,
                        - current + dfs(i + 1, True)
                    )
            cache[(index, turn)] = res
            return res
        
        result =  dfs(0, True)
        if result > 0:
            return "Alice"

        if result == 0:
            return "Tie"

        else:
            return "Bob"
                    
            
