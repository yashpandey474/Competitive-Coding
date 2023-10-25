class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        #1-DIGIT 2-DIGIT OR 3-DIGIT
        #ALL ALLOWED FOR SINGLE
        #0X NOT ALLOWED FOR DOUBLE
        #>255 NOT ALLOWED FOR TRIPLE

        #IMPOSSIBLE TO CREATE IF > 12 LEN
        if len(s) > 12:
            return []

        ans = []
        def backtrack(index, current, dots):
            #STRING EXHAUSTED OR DOTS EXHAUSTED
            if dots == 4 and index == len(s):
                #EXCEPT LAST DOT
                ans.append(current[:-1])
                return

            if dots > 4:
                return

            for i in range(index, min(len(s), index + 3)):
                #MAKE SURE NUMBER IS IN RANGE AND NO LEADING ZEROES
                if int(s[index:i+1]) < 256 and (index == i or s[index] != "0"):

                    backtrack(i+1, current + s[index:i+1] + ".", dots + 1)

        backtrack(0, "", 0)
        return ans


            
            

            
