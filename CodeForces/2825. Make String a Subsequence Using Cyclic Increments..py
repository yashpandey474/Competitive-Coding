#TAKEN FROM A SOLUTION ON LEETCODE

def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        if len(str1) < len(str2):
            return False
        
        pointer_pattern = 0
        for i in range(len(str1)):
            if pointer_pattern == len(str2):
                return True
            
            next_char = chr((ord(str1[i]) - ord('a') + 1)%26 + ord('a'))
            
            if (str1[i] == str2[pointer_pattern]):
                pointer_pattern += 1
            
            else:
                if next_char == str2[pointer_pattern]:
                    pointer_pattern += 1
            
        return pointer_pattern == len(str2)