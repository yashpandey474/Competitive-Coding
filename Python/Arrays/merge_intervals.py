class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        #SORT THE ARRAY OF INTERVALS
        intervals = sorted(intervals)
        answers = []
        #TRAVERSE
        for interval in intervals:
            #ANSWERS IS EMPTY OF END OF LAST INTERVAL IS LESS THAN CURRENT'S START
            if not answers or answers[-1][1] < interval[0]:
                answers.append(interval)
            
            else:
                answers[-1][1] = max(answers[-1][1], interval[1])
        
        return answers
