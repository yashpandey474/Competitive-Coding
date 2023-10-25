class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        target = "balloon"
        map_target = {}
        for i in target:
            if i not in map_target:
                map_target[i] = 0

            map_target[i] += 1

        #CHECK FREQUENCIES IN STRING
        map_string = defaultdict(int)
        for i in text:
            if i in map_target:
                if i not in map_string:
                    map_string[i] = 0

                map_string[i] += 1

        #CHECK CHARACTER WITH MINIMUM FREQUENCY
        min_len = float('inf')
        for i in map_target:
            min_len = min(min_len, map_string[i]//map_target[i])

        return min_len
