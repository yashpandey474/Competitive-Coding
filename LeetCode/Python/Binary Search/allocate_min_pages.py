class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return an integer
    
    
    def countStudents(self, maxPages, B, A):
        
        students = 1
        pages_allocatted = 0
        
        for i in A:
            #NOT POSSIBLE TO ALLOCATE ALL BOOKS
            if i > maxPages:
                return float('inf')
            
            #MOVE TO NEXT STUDENT
            if i + pages_allocatted > maxPages:
                students += 1
                pages_allocatted = i
            
            #CAN BE ALLOCATTED TO PREVIOUS STUDENT
            else:
                pages_allocatted += i
                
        return students
                                
	def books(self, A, B):
        
        #PERFORM BINARY SEARCH
        low = max(A)
        high = sum(A)
        
        #ITERATE FOR MAXIMUM NUMBER OF PAGES TO ANY STUDENT
        while low<=high:
            mid = (low+high)//2
            count = self.countStudents(mid, B, A)
            
            if count > B:
                low = mid + 1
            
            else:
                #ONE OF POSSIBLE ANSWERS
                high = mid-1

        return low
        
            
