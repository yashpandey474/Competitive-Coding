class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        store = set()

        if n <= 1:
            return n

        i = 0
        j = 0

        maxlen = 1

        while j < n:
            while i < j and s[j] in store:
                store.remove(s[i])
                i += 1

            store.add(s[j])
            maxlen = max(maxlen, j - i + 1)
            j += 1

        return maxlen

            