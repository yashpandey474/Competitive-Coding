    def kthElement(self,  arr1, arr2, n, m, k):
        count = 0
        i = 0
        j = 0
        n = len(arr1)
        m = len(arr2)
        while i<n and j<m:
            if arr1[i] <= arr2[j]:
                
                count+=1
                if count == k:
                    return arr1[i]
                i+=1
            
            else:
                
                count+=1
                if count == k:
                    return arr2[j]
                j+=1
        
