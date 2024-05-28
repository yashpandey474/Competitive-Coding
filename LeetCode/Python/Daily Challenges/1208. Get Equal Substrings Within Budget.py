class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)

        maxlen = 0

        i = 0
        j = 0

        currcost = 0

        while j < n:
            currcost += abs(ord(s[j]) - ord(t[j]))

            while i < j and currcost > maxCost:
                currcost -= abs(ord(s[i]) - ord(t[i]))
                i += 1

            if currcost <= maxCost:
                maxlen = max(maxlen, j - i + 1)
            j += 1

        return maxlen

            