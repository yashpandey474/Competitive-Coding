class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        #BINARY SEARCH ON THE MAXIMUM SUM OF SUBARRAYS
        low = max(nums)
        high = sum(nums)
        #ASSUME THE WORST
        result = high

        #FIND IF ARRAY CAN BE SPLIT
        def canSplit(largest):
            #COUNT SUBARRAYS
            subarray = 1
            #CURRENT SUM
            curSum = 0

            for n in nums:
                curSum += n
                if curSum > largest:
                    subarray += 1
                    #N IS SEPARATE SUBARRAY
                    curSum = n

            #CAN SPLIT
            return subarray <= k

        while low <= high:
            #AVOID OVERFLOW
            mid = low + ((high - low)//2)

            #CHECK IF VALID TO SPLIT
            if canSplit(mid):
                #SMALLER RESULT
                result = mid
                high = mid - 1

            else:
                #LOOK FOR WORSE RESULTS
                low = mid + 1

        
        return result
