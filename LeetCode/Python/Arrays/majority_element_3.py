class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #MAXIMUM 2 ELEMENTS
        if not nums:
            return []

        candidate1 = 0
        candidate2 = 1
        count1 = 0
        count2 = 0
        
        #FIRST PASS
        for i in nums:
            if i == candidate1:
                count1 += 1
            
            elif i == candidate2:
                count2 += 1
            
            elif count1 == 0:
                candidate1, count1 = i, 1
            
            elif count2 == 0:
                candidate2, count2 = i, 1

            else:
                count1, count2 = count1 - 1, count2 - 1
            
        #SECOND PASS
        return [n for n in (candidate1, candidate2)
        if nums.count(n) > len(nums)//3
        ]
            
