class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        n1 = len(str1)
        n2 = len(str2)

        if n2 > n1:
            str1, str2 = str2, str1
        
        for i in range(n2, 0, -1):
            temp_string = str2[:i]

            if temp_string * (len(str2)//len(temp_string)) == str2 and temp_string * (len(str1)//len(temp_string)) == str1:
                return temp_string

        return ""
