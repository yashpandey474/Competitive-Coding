class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        cache = {}
        result = []

        def dfs(index, current):
            if index >= len(s):
                if current:
                    result.append(current.rstrip())

            for i in range(index, len(s)):
                if s[index:i+1] in wordDict:
                    dfs(i + 1, current + s[index:i + 1] + " ")

            return

        dfs(0, "")
        return result
