class Solution(object):

    def countPairs(self, arr1, start1, end1, arr2, start2, end2):
        right = start2
        for i in range(start1, end1+1):

            while right <= end2 and arr1[i] > 2*arr2[right]:
                right+=1
            self.ans += right - start2

    def merge(self, arr1, start1, end1, arr2, start2, end2):
        i = start1
        j = start2
        arr3 = []

        while i<=end1 and j<=end2:
            if arr1[i] <= arr2[j]:
                arr3.append(arr1[i])
                i+=1
            else:
                arr3.append(arr2[j])
                j+=1
        
        arr3.extend(arr1[i:end1+1])
        arr3.extend(arr2[j:end2+1])
        arr1[start1:end2+1] = arr3[:]
        return

    def mergeSort(self, nums, start, end):
        if start < end:
            mid = (start+end)//2
            self.mergeSort(nums, start, mid)
            self.mergeSort(nums, mid+1, end)
            self.countPairs(nums, start, mid, nums, mid+1, end)
            self.merge(nums, start, mid, nums, mid+1, end)

    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.ans = 0
        self.mergeSort(nums, 0, len(nums)-1)
        return self.ans
