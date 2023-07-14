#KEEP TWO ARRAYS: ONE PREVIOUS AND ONE CURRENT
#FOR CURRENT; ADD 1 AT START AND 1 AT END. FOR MIDDLE ELEMENTS; ADD SUMS FROM PREVIOUS ARRAY
class Solution(object):

    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []

        if numRows == 0:
            return self.result

        previous = [1]
        result.append(previous)

        for i in range(2, numRows+1):
            current = [1]
            for j in range(0, len(previous)-1):
                current.append(previous[j]+previous[j+1])
            
            current.append(1)

            result.append(current)

            previous = current
        
        return result


