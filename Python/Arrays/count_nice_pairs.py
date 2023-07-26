class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        #FIND THE REVERSE OF INTEGER
        def reverse(number):
            result = 0 
            while number > 0:
                x = number % 10
                result = result * 10 + x
                number = number // 10

            return result

        #COUNT PAIRS HAVING SAME NUMS[I] - REV[I]
        map_freq = {}

        #STORE THE VALUE AND FREQUENCY
        for i in range(len(nums)):
            val = nums[i] - reverse(nums[i])
            if val not in map_freq:
                map_freq[val] = 0

            map_freq[val] += 1

        #COUNT NUMBER OF PAIRS THAT CAN BE MADE
        result = 0
        for i in map_freq.values():
            #FREQ * (FREQ - 1) //2
            result += i*(i-1)//2 

        #RETURN RESULT%MOD
        return result%(10**9+7)
