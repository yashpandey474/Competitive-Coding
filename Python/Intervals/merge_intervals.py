class Solution:

    def mergeIntervals(self, int1, int2):
        if int1[1] < int2[0] or int1[0] > int2[1]:
            return False

        return True
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #SORT THE INTERVALS ON START TIME
        intervals = sorted(intervals, key = lambda x: x[0])
        result = []
        for i in range(len(intervals)):
            if not result or not self.mergeIntervals(result[-1], intervals[i]):
                result.append(intervals[i])

            else:
                result[-1] = [
                    min(
                    result[-1][0],
                    intervals[i][0]
                    ),
                    max(
                        result[-1][1],
                        intervals[i][1]
                    )
                ]


        return result
