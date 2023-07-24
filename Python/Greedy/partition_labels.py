class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        #CREATE ARRAY OF FIRST OCCURENCE AND LAST OCCURENCE OF CHARACTERS
        map_first_last = {}

        for i in range(len(s)):
            if s[i] in map_first_last:
                map_first_last[s[i]][1] = i

            else:
                map_first_last[s[i]] = [i, i]


        intervals = []
        for first, last in sorted(map_first_last.values()):
            if not intervals or intervals[-1][1] < first:
                intervals.append([first, last])

            else:
                intervals[-1][1] = max(intervals[-1][1], last)
                continue


        print(intervals)
        print(map_first_last)

        return [intervals[i][1]-intervals[i][0]+1 for i in range(len(intervals))]

        
                
