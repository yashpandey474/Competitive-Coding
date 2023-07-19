class Solution:

    def isPalindrome(self, s, start, end):
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1

        return True
                

    def recursion(self, s, ans, index):
        
        #IF WHOLE STRING CONSIDERED
        if index == len(s):
            #ADD ANSWER
            self.result.append(ans)
            #RETURN
            return

        else:

            for i in range(index, len(s)):
                #CHECK IF SUBSTRING IS A PALINDROME
                if self.isPalindrome(s, index, i):
                    self.recursion(s, ans + [s[index:i+1]], i+1)

        #GO FROM INDEX UP TILL ALL POINTS WHERE IT IS A PALINDROME

    def partition(self, s: str) -> List[List[str]]:
        self.result = []
        
        self.recursion(s, [], 0)

        return self.result
