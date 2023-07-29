class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        cache = {}
        events = sorted(events)

        def dfs(index, num, maxDay):
            if index >= len(events) or num >= k:
                return 0

            if (index, num, maxDay) in cache:
                return cache[(index, num, maxDay)]

            res = 0
            #IF MAXIMUM ENDING DAY IS BEFORE CURRENT START DAY
            if maxDay < events[index][0]:
                #CAN ATTEND
                res = max(
                    dfs(index + 1, num, maxDay),
                    dfs(index + 1, num + 1, events[index][1]) + events[index][2]
                )

            else:
                #CANNOT ATTEND
                res = dfs(index + 1, num, maxDay)

            cache[(index, num, maxDay)] = res
            return res

        return dfs(0, 0, 0)
