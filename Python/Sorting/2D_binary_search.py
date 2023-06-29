def search_shipment(matrix, identifier):
    #IMPLEMENT BINARY SEARCH CONSIDERING THE MATRIX LIKE A 1D ARRAY
    left = 0
    rows = len(matrix)
    cols = len(matrix[0])
    right = rows*cols-1
    
    while(left<=right):
        mid = (left + right)//2 #NEAREST INTEGER: FLOOR DIVISION
        
        #ROW = QUOTIENT AND COLUMN = REMAINDER
        element = matrix[mid // rows][mid%cols]
        
        if(element < identifier):
            left = mid+1
        
        elif (element > identifier):
            right = mid-1
        else:
            return True
    return False
