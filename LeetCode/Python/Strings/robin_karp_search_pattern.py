from typing import List

'''
SIMPLE PATTERN MATCHING ALGORITHM
1. KEEP A SLIDING WINDOW OF SIZE OF PATTERN
2. MATCH THE HASH OF SUBSTRING TO HASH OF PATTERN
3. IF HASH MATCHES; MATCH THE EXACT TEXT
4. ADD THE STARTING INDEX TO RESULT
'''

def stringMatch(text: str, pattern: str) -> List[int]:
    # Write your code here.

    #ROBIN-KARP ALGORITHM
    #KEEP A SLIDING WINDOW IN TEXT OF THE SIZE OF PATTERN
    #HASH THE PATTERN TEXT AND THE WINDOW TEXT
    #IF HASHES MATCH; CHECK FOR EXACT MATCH

    i = 0
    m = len(pattern)
    n = len(text)
    text_hash = hash(text[i:m])
    pattern_hash = hash(pattern)
    result = []
    #MAXIMUM INDEX OF STARTING OF WINDOW
    while i < n - m + 1:
        if text_hash == pattern_hash and text[i:i+m] == pattern:
            result.append(i+1)

        i += 1
        text_hash = hash(text[i:i+m])

    return result

