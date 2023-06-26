class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))

        if(len(nums) < 3):
            return  max(nums)


        numsneg = [-a for a in nums]

        heapq.heapify(numsneg)
        max1 = heapq.heappop(numsneg)
        max2 = heapq.heappop(numsneg)
        return -heapq.heappop(numsneg)
