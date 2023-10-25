class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if(len(s) <= 1):
            return len(s)

        start = 0
        end = 1
        set_char = [s[start]]
        current_len = 1
        max_len = 1

        

        while(start<=end and  end<len(s)):
            if(s[end] in set_char):
                max_len = max(max_len, current_len)
                current_len -=1
                set_char.remove(s[start])
                start +=1

            else:
                set_char.append(s[end])
                current_len += 1
                end+=1
        

        return max(max_len, current_len)
