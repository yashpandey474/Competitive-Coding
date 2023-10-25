class Solution:


    def isSafe(self, row, col, ans, n):
        dupRow = row
        dupCol = col

        #CHECK UPPER DIAGONAL
        while row>=0 and col>=0:
            if ans[col][row] == 'Q':
                return False
            row-=1
            col-=1

        row = dupRow
        col = dupCol
        #CHECK LOWER DIAGNOAL
        while row<n and col>=0:
            if ans[col][row] == 'Q':
                return False
            row+=1
            col-=1

        #CHECK CURRENT ROW
        col = dupCol
        row = dupRow
        while col>=0:
            if ans[col][row] == 'Q':
                return False
            col-=1
        
        #QUEEN CAN BE PLACED HERE
        return True



    def solve(self, n, col, solutions, ans):
        #ALL QUEENS PLACED
        if col == n:
            #RETURN WITH COMPLETED BOARD
            print(solutions)
            newSolutions = solutions[:]
            ans.append(newSolutions)
            return 

        #CHECK FOR EACH ROW ON THE COLUMN
        for row in range(n):

            #CHECK IF SAFE
            if self.isSafe(row, col, solutions, n):
                #DEFINE
                solutions[col] = solutions[col][:row] + 'Q' + solutions[col][row+1:]
                
                #RECURSE FOR NEXT QUEEN
                self.solve(n, col+1, solutions, ans)
                #BACKTRACK
                solutions[col] = solutions[col][:row] + '.' + solutions[col][row+1:]

    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        solutions = ['.'*n for _ in range(n)]

        #BOARD CREATED
        #ATTEMPT TO SOLVE [START WITH 0TH COLUMN]
        self.solve(n, 0, solutions, ans)
        return ans
