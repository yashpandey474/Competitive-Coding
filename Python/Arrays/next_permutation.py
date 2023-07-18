class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        #FOLLOWING ALGORITHM FROM WIKIPEDIA

        #FIND K
        n = len(nums)
        k = -1
        for i in range(n):
            if i != n-1 and nums[i] < nums[i+1]:
                k = i
        print("K = ", k)
        #K DOES NOT EXIST
        if k == -1:
            nums.reverse()
        
        else:
            #FIND L
            l = -1
            for i in range(n):
                if nums[i] > nums[k]:
                    l = i
            
            print("L =", l)
            #SWAP NUMS[K] AND NUMS[L]
            nums[k], nums[l] = nums[l], nums[k]

            #REVERSE ARRAY AFTER
            nums[k+1:] = reversed(nums[k+1:])

