class Solution:
    def characterReplacement(self, st: str, k: int) -> int:
        def help(s):
            res, count = 0, 0
            dic = {}
            l = 0
            temp = k
            for r in s:
                count += 1
                dic[r] = dic.get(r, 0) + 1
                while count - max(dic.values()) > k:
                    dic[s[l]] -= 1
                    l += 1
                    count -= 1
                res = max(res,count)
            return res
        return max(help(st),help(st[::-1]))