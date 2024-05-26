class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        map1 = {}
        map2 = {}

        n1 = len(s1)
        n2 = len(s2)

        if n1 > n2:
            return 0

        for i in s1:
            if i not in map1:
                map1[i] = 0

            map1[i] += 1

        map2 = map1.copy()

        

        i = 0
        j = 0

        while j < n2:
            if s2[j] not in map1:
                map1 = map2.copy()
                j += 1
                i = j
                continue

            map1[s2[j]] -= 1    

            while map1[s2[j]] < 0:
                map1[s2[i]] += 1
                i += 1
            
            if max(map1.values()) == 0:
                return 1
            j += 1

        return 0

            
