class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        
        #STORE CHARACTERS ON LEFT OF MID
        leftSet = set()

        #STORE CHARACTERS ON RIGHT OF MID
        rightSet = collections.Counter(s)

        #STORE PALINDROMES
        palindromes = set()

        #ITERATE THROUGH POSSIBLE MIDS
        for i in range(len(s)):
            rightSet[s[i]] -= 1
            if rightSet[s[i]] == 0:
                del rightSet[s[i]]

            #ITERATE THROUGH POSSIBLE OUTS
            for c in range(ord('a'), ord('z') + 1):
                ch = chr(c)
                if ch in leftSet and ch in rightSet:
                    palindromes.add((s[i], ch))

            #UPDATE LEFT AND RIGHT SETS
            leftSet.add(s[i])
                

        return len(palindromes)
            
