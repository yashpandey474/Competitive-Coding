class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        half = total // 2

        #RUN BINARY SEARCH ON SMALLER ARRAY
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        #BINARY SEARCH 
        l = 0
        r = len(nums1) - 1

        while True:
            midA = (l + r)//2
            midB = half - midA - 2

            #HANDLE OUT OF BOUNDS
            Aleft = nums1[midA] if midA >= 0 else -float('inf')
            Aright = nums1[midA + 1] if midA < len(nums1) - 1 else float('inf')

            Bleft = nums2[midB] if midB >= 0 else -float('inf')
            Bright = nums2[midB + 1] if midB < len(nums2) - 1 else float('inf')

            #CHECK IF CORRECT PARTITION
            if Aleft <= Bright and Bleft <= Aright:
                #ODD
                if total % 2:
                    return min(Aright, Bright)

                #EVEN
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2

            elif Aleft > Bright:
                #TOO MANY ELEMENTS FROM A
                r = midA - 1

            else:
                #TOO LESS ELEMENTS FROM A
                l = midA + 1
