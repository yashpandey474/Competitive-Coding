class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map_anagrams = {}

        for i in strs:
            sorted_i = tuple(sorted(i))

            if sorted_i in map_anagrams:
                map_anagrams[sorted_i].append(i)

            else:
                map_anagrams[sorted_i] = [i,]

        result = []
        for i in map_anagrams:
            result.append(map_anagrams[i])
        return result
