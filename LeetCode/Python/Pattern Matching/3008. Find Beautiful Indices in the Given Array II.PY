class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:

        ans = []
        a1 = []
        b1 = []
        
        base = 256
        modulus = 1111111117777777
        h1 = pow(base, len(a) - 1)
        h2 = pow(base, len(b) - 1)

        
        def getHash(string):
            current = 0
            orda = ord('a')
            
            for c in string:
                current *= base
                current += (ord(c) - orda) + 1
                current %= modulus
                
            return current
                
        def matches(string, pattern):
            pat_hash = getHash(pattern)
            m = len(pattern)
            res = []
            h = pow(base, m, modulus)
            
            current = 0
            orda = ord("a")
            
            for index, c in enumerate(string):
                current *= base
                current += (ord(c) - orda) + 1
                
                # print(current, pat_hash)
                if index >= m:
                    current -= h*(ord(string[index - m]) - orda + 1)
                current %= modulus
                
                if index >= m - 1 and current == pat_hash:
                    res.append(index - m + 1)

                
            return res
                    
            
        a1 = matches(s, a)
        b1 = matches(s, b)
        
        # print(a1, b1)
                
        i = 0
        j = 0
        while i < len(a1) and j < len(b1):
            if abs(a1[i] - b1[j]) <= k:
                ans.append(a1[i])
                i += 1
                
            elif a1[i] - b1[j] > k:
                j += 1
                
            elif b1[j] - a1[i] > k:
                i += 1
                
        return ans