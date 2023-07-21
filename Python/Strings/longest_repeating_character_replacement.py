'''
SLIDING WINDOW PROBLEM
1. KEEP A MAP OF FREQUENCIES OF ELEMENTS
2. WINDOW IS VALID: IF LENGTH - MAX FREQ <=  K: MOVE RIGHT FORWARD
3. WINDOW IS INVALID: DECREMEENT FREQ OF LEFT ELEMENT AND MOVE LEFT FORWARD
'''

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0
        j = 1
        #CREATE A MAP TO HOLD FREQUENCIES
        map_freq = {}
        #SET FREQUENCY OF FIRST ELEMENT
        map_freq[s[0]] = 1
        max_len = 1

        #SLIDING WINDOW RIGHT POINTER
        while j<len(s):
            #VALID WINDOW: LENGTH OF WINDOW - 
            if s[j] in map_freq:
                #INCREEMENT COUNT OF CURRENT
                map_freq[s[j]]+=1

            #ADD CURRENT CHARACTER TO MAP
            elif s[j] not in map_freq:
                map_freq[s[j]] = 1

            #VALID WINDOW:OTHER CHARACTERS LESS THAN K
            if (j-i+1) - max(map_freq.values()) <= k:
                #UPDATE LENGTH AND MOVE RIGHT FORWARD
                max_len = max(max_len, j-i+1)
                j+=1
            #INVALID WINDOW
            #INVALID WINDOW: REMOVE LEFT CHARACTER AND MOVE IT FORWARD
            else:
                map_freq[s[i]]-=1
                i+=1

        return max_len


