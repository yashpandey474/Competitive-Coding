class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        result = []
        for i in range(0, len(board)):
            for j in range(0, len(board[i])):
                element = board[i][j]
                if(element != "."):
                    result.append((i, ""+element))#ROW
                    result.append((""+element, j))#COLUMN
                    result.append((i//3, j//3, element))
                    
        print(result)
        return len(result) == len(set(result))
