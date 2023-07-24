class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:

        #SIMILAR TO HOUSE ROBBER PROBLEM
        n = len(nums)
       #SORT THE ARRAY: GET NUMS[I], NUMS[I]+1 CLOSE TOGETHER

       #CREATE A MAP OF COUNTS
        map_freq = {}

        for i in nums:
            if i in map_freq:
               map_freq[i] += 1

            else:
                map_freq[i] = 1

        nums = sorted(list(set(nums)))
        earn1, earn2 = 0, 0
        for i in range(0, len(nums)):
            #ALL TO DELETE AND CURRENT
            curEarn = nums[i] * map_freq[nums[i]]
            print("CUR = ", curEarn, "EARN1 = ", earn1, "EARN2 = ", earn2)
            if i>0 and nums[i] == nums[i-1] + 1:
                temp = earn2
                earn2 = max(curEarn + earn1, earn2)
                earn1 = temp
            else:
                temp = earn2
                earn2 = curEarn + earn2
                earn1 = temp
        return earn2
