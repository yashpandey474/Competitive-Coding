class Solution:
    def isSafe(self, n, row, col, result):
        dupRow = row
        dupCol = col

        while row>=0 and col >= 0:
            if result[col][row] == 'Q':
                return False
            row -= 1
            col -=1 
        
        row = dupRow
        col = dupCol


        while col>=0:
            if result[col][row]== 'Q':
                return False
            col-=1

        col = dupCol
        
        while row < n and col >=0:
            if result[col][row] == 'Q':
                return False
            col-=1
            row += 1
        
        return True

    def recursion(self, n, col, result):
        if col == n:
            self.ans += 1
            return

        for row in range(n):
            if self.isSafe(n, row, col, result):
                result[col] = result[col][:row] + 'Q' + result[col][row+1:]
                self.recursion(n, col+1, result)
                result[col] = result[col][:row] + '.' + result[col][row+1:]


    def totalNQueens(self, n: int)-> int:
        self.ans = 0
        result = ['.'*n for _ in range(n)]
        self.recursion(n, 0, result)
        return self.ans
