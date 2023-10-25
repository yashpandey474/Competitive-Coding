class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #USE CONCEPT OF PREFIX SUM AND A HASH MAP
        prefix = [0]*len(nums)
        prefix_map = {}
        answer = 0
        prefix[0] = nums[0]

        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] + nums[i]

        #CHECK FOR K
        for i in range(len(nums)):
            if prefix[i] == k:
                answer += 1
            
            if prefix[i]-k in prefix_map:
                answer += prefix_map[prefix[i]-k]
            
            if prefix[i] not in prefix_map:
                prefix_map[prefix[i]]  = 1
            else:
                prefix_map[prefix[i]] += 1
        
        return answer

