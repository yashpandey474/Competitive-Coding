class Solution:
	# @param A : list of integers
	# @return a list of integers
	def prevSmaller(self, A):
        
        if len(A) == 0:
            return []
            
        
        n = len(A)
        answer = [-1]*n
        stack = []
        
        for i in range(0, n):

            ele = A[i]
        
            while stack:
                if stack and stack[-1] < ele:
                    answer[i] = stack[-1]
                    break 
                stack.pop()
            stack.append(A[i])
            
        return answer
            
