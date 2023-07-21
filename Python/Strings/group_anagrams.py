from typing import List

    
    
def group_anagrams(words: List[str]) -> List[List[str]]:
    #MAP FOR ANAGRAMS
    anagrams = {}
    
    for word in words:
        #CREATE A STRING FROM SORTED CHARACTERS
        sorted_word = ' '.join(sorted(word))
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word,]
            
    #RETURN THE VALUES IN A LIST
    return list(anagrams.values())
    
