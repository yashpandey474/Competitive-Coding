class Meeting:
    def __init__(self, number, start, end):
        self.start = start
        self.end = end
        self.number = number
class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def insertInPlace(self, arr, element):
        index = 0
        while index < len(arr) and arr[index].end < element.end:
            index += 1
        arr.insert(index, element)
        
    def maximumMeetings(self,n,start,end):
        # code here
        answer = 0
        meetings = []
        
        #CREATE MEETINGS & SORT ON END TIME
        for i in range(n):
            self.insertInPlace(meetings, Meeting(i, start[i], end[i]))
        
        #ONE PASS: KEEP LIMIT OF END TIME
        end_time = 0
        for i in meetings:
            if i.start > end_time:

                answer += 1
                end_time = max(i.end, end_time)
            
            else:
                continue
        return answer
       
