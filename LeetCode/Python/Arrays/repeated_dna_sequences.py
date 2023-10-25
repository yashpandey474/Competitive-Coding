class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        st = 0
        en = 10
        result = set()
        set_substring = set()

        while en < len(s) + 1:
            substring = s[st: en]
            if substring in set_substring:
                result.add(substring)
            else:
                set_substring.add(substring)

            st += 1
            en += 1

        return list(result)
