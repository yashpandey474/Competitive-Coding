class Solution:
    map_number_to_letters = {
            "1": [],
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        };
    def numberToCharacter(self, digit):
        return chr(int(digit) + 96)
    def recursion(self, digits: str, answer: str):
        if not digits:
            self.res.append(answer)
            return
        ckeys = self.map_number_to_letters[digits[0]]
        for key in ckeys:
            self.recursion(digits[1:], answer+key)
            
    def letterCombinations(self, digits: str) -> List[str]:
        #EMPTY STRING
        if not digits:
            return []

        self.res = []
        self.recursion(digits, '')
        return self.res
    

        
        
