class Solution:
    def longestValidParentheses(self, s: str) -> int:

        cache = {}
        stack = []

        for i in range(len(s)):
            #IF OPENING: ADD TO STACK
            if s[i] == '(':
                #APPEND THE INDEX
                stack.append(i)

            elif stack:
                    #LAST OPENING BRACKET
                start = stack.pop()

                    #LONGEST VALID LENGTH HERE
                cache[i] = i - start + 1

                    #IF A VALID ONE WAS FORMED BEFORE
                if start - 1 in cache:
                    cache[i] += cache[start-1]

        #RETURN MAX LENGTH
        if not cache:
            return 0
        return max(cache.values())
