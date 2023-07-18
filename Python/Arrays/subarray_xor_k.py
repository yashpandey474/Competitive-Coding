class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        if not A:
            return 0
            
        xor_index = {}
        ans = 0
        prefix_xor = 0
        xor_index[prefix_xor] = 1
        
        for i in range(len(A)):
            #CALCULATE CURRENT XOR
            prefix_xor = prefix_xor ^ A[i]
            
            #NEED TO FIND XOR
            find_xor = prefix_xor ^ B
            
            if find_xor in xor_index:
                ans += xor_index[find_xor]
            
            if prefix_xor in xor_index:
                xor_index[prefix_xor] += 1
            
            else:
                xor_index[prefix_xor] = 1
                
        return ans
                
            
            
            
            
