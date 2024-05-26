class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)

        dp = [0 for i in range(n + 1)]

        dp[n] = 1

        res = []
        
        sp = [set() for i in range(n)]

        wordDict = set(wordDict)

        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i:j + 1] in wordDict and dp[j + 1]:
                    sp[i].add(j)
                    dp[i] = 1

        def backtrack(index, path):
            if index == n:
                if path:
                    res.append(path.lstrip())
                return

            for end in sp[index]:
                backtrack(end + 1, path + " " + s[index:end + 1])

        if dp[0]:
            backtrack(0, "")
        return res