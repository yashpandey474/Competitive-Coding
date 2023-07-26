class Solution:
    def mergeInterval(self, inter1, inter2):
        if inter2[1] < inter1[0] or inter2[0] > inter1[1]:
            return False

        return True

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        #SIMILAR TO INSERTION SORT
        
        result = []
        for i in range(len(intervals)):
            #FIRST NON OVERLAPPING
            if newInterval[1] < intervals[i][0]:
                result.append(newInterval)
                result.extend(intervals[i:])
                return result

            #AFTER CURRENT INTERVAL
            if newInterval[0] > intervals[i][1]:
                result.append(intervals[i])
            
            #OVERLAPPING INTERVAL
            else:
                newInterval[0] = min(intervals[i][0],
                newInterval[0])
                newInterval[1] = max(intervals[i][1],
                newInterval[1])

        result.append(newInterval)
        return result

            

