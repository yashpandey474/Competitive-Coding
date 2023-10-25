class Solution:
    def dfs(self, board, word, row, column, visited):
        if len(word)==0:
            return True

        visited.add((row, column))

        if row>0 and board[row-1][column] == word[0]:
            if (row-1, column) not in visited:
                if(self.dfs(board, word[1:], row-1, column, visited)):
                    return True

        if row <len(board)-1 and board[row+1][column] == word[0] and (row+1, column) not in visited:
            if self.dfs(board, word[1:], row+1, column, visited):
                return True

        if column>0 and board[row][column-1] == word[0]:
            if (row, column-1) not in visited:
                if self.dfs(board, word[1:], row, column-1, visited):
                    return True

        if column <len(board[0])-1 and board[row][column+1] == word[0] and (row, column+1) not in visited:
            if self.dfs(board, word[1:], row, column+1, visited):
                return True

        visited.remove((row, column))
        return False

        
        
    def exist(self, board: List[List[str]], word: str) -> bool:

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:

                    if(self.dfs(board, word[1:], i, j, set())):
                        return True

        return False
