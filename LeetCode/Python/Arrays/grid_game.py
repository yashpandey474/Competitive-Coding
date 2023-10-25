class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        cols = len(grid[0])

        pre1 = grid[0].copy()
        pre2 = grid[1].copy()

        #COMPUTE THE PREFIX SUMS
        for i in range(1, cols):
            pre1[i] += pre1[i - 1]
            pre2[i] += pre2[i - 1]

        #FIND MINIMUM POINTS 2ND CAN COLLECT
        result = float('inf')

        for i in range(cols):
            top = pre1[-1] - pre1[i]
            bottom = pre2[i - 1] if i > 0 else 0
            secondRobot = max(top, bottom)
            result = min(result, secondRobot)

        return result
