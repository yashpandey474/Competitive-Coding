class Solution:
    def minWindow(self, s: str, t: str) -> str:

        #HASH MAP FOR PATTERN
        map_pattern = {}
        for i in t:
            if i in map_pattern:
                map_pattern[i] += 1
            else:
                map_pattern[i] = 1

        #HASH MAP COUNTS FOR STRING
        have = 0
        need = len(map_pattern.keys())
        map_string = {}
        for i in map_pattern.keys():
            map_string[i] = 0

        #MAINTAIN A SLIDING WINDOW
        i = 0
        j = 0
        ans = ""
        while j<len(s):
            if s[j] in map_string:
                map_string[s[j]]+=1
                if map_string[s[j]] == map_pattern[s[j]]:
                    have += 1

            while have == need:
                if ans == "" or j-i+1 < len(ans):
                    ans = s[i:j+1]

                if s[i] in map_string:
                    map_string[s[i]]-=1
                    if map_string[s[i]] < map_pattern[s[i]]:
                        have -= 1

                i+=1

            
            j+=1

        return ans


            
