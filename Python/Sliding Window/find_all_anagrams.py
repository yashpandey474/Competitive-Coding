class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        map_p = defaultdict(int)
        map_s = defaultdict(int)
        result = []
        n = len(s)
        m = len(p)

        if n < m:
            return []

        #INITIALISE POINTERS
        for i in range(m):
            map_p[p[i]]+=1
            map_s[s[i]]+=1

        #CHECK MATCHES
        matches = 0
        for i in range(ord('a'), ord('z')+1):
            if map_p[chr(i)] == map_s[chr(i)]:
                matches += 1

        if matches == 26:
            result.append(0)

        st = 0
        en = m
        while en < n:
            map_s[s[en]] += 1
            if map_s[s[en]] == map_p[s[en]]:
                matches += 1
            if map_s[s[en]] == map_p[s[en]] + 1:
                matches -= 1

            map_s[s[st]] -= 1
            if map_s[s[st]] == map_p[s[st]]:
                matches += 1

            if map_s[s[st]] == map_p[s[st]] - 1:
                matches -= 1

            st += 1
            en += 1

            if matches == 26:
                result.append(st)

        return result

            

        

    
