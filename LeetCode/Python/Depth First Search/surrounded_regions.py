class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        #CHANGE ALL UNSURROUNDED REGIONS TO T
        rows, columns = len(board), len(board[0])

        def dfs(row, column):
            if row < 0 or column < 0 or row >= rows or column >= columns or board[row][column] != 'O':
                return

            board[row][column] = "T"
            dfs(row + 1, column)
            dfs(row, column + 1)
            dfs(row - 1, column)
            dfs(row, column - 1)
            return

        

        for i in range(rows):
            for j in range(columns):
                if board[i][j] == 'O' and (i == rows-1 or i == 0 or j == columns-1 or j == 0):
                    dfs(i, j)

        print(board)
        #CHANGE ALL SURROUNDED REGIONS TO X
        for i in range(rows):
            for j in range(columns):
                if board[i][j] == "O":
                    board[i][j] = "X"

        for i in range(rows):
            for j in range(columns):
                if board[i][j] == "T":
                    board[i][j] = "O"
