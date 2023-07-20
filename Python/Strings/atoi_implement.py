class Solution:
    def myAtoi(self, s: str) -> int:
        result = 0
        sign = 1

        #ITERATE THROUGH THE STRING
        for i in s:
            #CHECK IF IT IS A DIGIT
            if i>='1' and i<='9':
                result = result*10 + int(i)
                continue

            if i == '-':
                sign = -1
                continue

            elif i != ' ' and i != '+':
                break

        if result*sign < -pow(2, 31):
            return -pow(2, 31)

        if result*sign > pow(2, 31)-1:
            return pow(2, 31) - 1
        return result*sign
