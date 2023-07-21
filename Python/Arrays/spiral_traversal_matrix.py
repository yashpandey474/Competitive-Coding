class Solution:
    def dfs(self, matrix, result, top, bottom, left, right):
        while top<=bottom and left<=right:
            #PRINT FROM LEFT TO RIGHT
            for i in range(left, right+1):
                result.append(matrix[top][i])

            #INCREMENT
            top += 1

            #PRINT FROM TOP TO BOTTOM
            for i in range(top, bottom+1):
                result.append(matrix[i][right])
            
            #DECREMENT RIGHT
            right -= 1

            if top<= bottom:
                #PRINT FROM RIGHT TO LEFT
                for i in range(right, left-1, -1):
                    result.append(matrix[bottom][i])

                #DECREMENT BOTTOM
                bottom -= 1

            if left <= right:
                #PRINT FROM BOTTOM TO TOP
                for i in range(bottom, top-1, -1):
                    result.append(matrix[i][left])

                #INCREMENT LEFT
                left += 1

        
        

        
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        rows = len(matrix)
        columns = len(matrix[0])
    
        self.dfs(matrix, result, 0, rows-1, 0, columns-1)

        return result
