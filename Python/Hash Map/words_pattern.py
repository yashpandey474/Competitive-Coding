class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        map1 = {}
        map2 = {}
        words = s.split()

        if len(words) != len(pattern):
            return False
            
        for i in range(len(pattern)):
            if(pattern[i] in map1):
                if map1[pattern[i]] != words[i]:
                    return False
            if(words[i] in map2):
                if map2[words[i]] != pattern[i]:
                    return False
            else:
                map1[pattern[i]] = words[i]
                map2[words[i]] = pattern[i]

        return True
