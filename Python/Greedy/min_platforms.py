class Activity:
    def __init__(self, start, end):
        self.start = start
        self.end = end


def maximumActivities(start, finish):
    # Write your Code here.

    #CREATE SORTED ACTIVITY ARRAY
    n = len(finish)
    acts = list(zip(start, finish))
    acts = sorted(acts, key = lambda x: x[1])
    
    #ITERATE AND FIND
    limit = 0
    answer = 0
    for i in acts:
        if i[0] > limit:
            answer += 1
            limit = max(limit, i[1])
        else:
            continue
    return answer
