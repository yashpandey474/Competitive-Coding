class Solution:
    def recursion(self, string, open, close, limit):
        #BASE CASE: ALL ADDED
        if open == limit and close == limit:
            self.ans.append(string)
            return
        
        #TWO CHOICES AT EACH STEP

        #ADD OPEN WHEN LESS THAN LIMIT
        if open < limit:
            self.recursion(string + "(", open+1, close, limit)
        
        #ADD CLOSE WHEN LESS THAN OPEN
        if close < open:
            self.recursion(string + ")", open, close + 1, limit)
    def generateParenthesis(self, n: int) -> List[str]:
        self.ans = []
        #STRING, OPEN, CLOSE, LIMIT
        self.recursion( "", 0, 0, n)
        return self.ans
