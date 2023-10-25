class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:


        #ITERATE AND COMPARE ALL ADJACENT WORDS
        for i in range(1, len(words)):
            #WORD1 AND WORD2
            word1 = words[i-1]
            word2 = words[i]


            #ITERATE TO FIND IF ORDER IS CORRECT
            i = 0
            j = 0
            while i < len(word1) and j<len(word2):
                if word1[i] == word2[j]:
                    i += 1
                    j += 1
                elif order.index(word1[i]) > order.index(word2[j]):
                    return False
                elif order.index(word1[i]) < order.index(word2[j]):
                    break
                
                
            else:
                if i != len(word1) and j == len(word2):
                    return False

        return True
