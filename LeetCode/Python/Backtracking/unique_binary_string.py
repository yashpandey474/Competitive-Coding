class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        strSet = {s for s in nums}

        def dfs(index, string):
            if index == n:
                res = "".join(string)
                if res not in strSet:
                    return res
                return None
            
            #STAY POSITION AS 0
            res = dfs(index+1, string)
            if res: return res
            #SET THE BIT
            string[index] = "1"
            res = dfs(index+1, string)
            if res: return res



        #INDEX AND STRING [AS LIST TO MODIFY]
        return dfs(0,["0" for s in nums])
