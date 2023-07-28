'''
1. SORT THE TICKETS SO THAT ADJ LISTS ARE SORTED
2. ADD START POINT TO RESULT
3. RUN DFS ON THE START
4. FOR EACH ADJACENT NODE; REMOVE IT FROM THE ADJ LIST AND ADD TO RESULT
5. IF THE DFS RETURNS TRUE [ALL NODES ADDED]: RETURN TRUE
6. IF DFS RETURNS FALSE; CANNOT ADD ALL; BACKTRACK BY ADDING IT TO THE ADJ LIST AND REMOVING FROM RESULT
7. RETURN THE RESULT ARRAY AS ONE SOLUTION MUST EXIST
'''

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        #CREATE A GRAPH FROM TICKETS
        graph = defaultdict(list)

        #SORT THE TICKETS FOR THE ADJ LISTS TO BE SORTED
        tickets = sorted(tickets)

        for ticket in tickets:
            graph[ticket[0]].append(ticket[1])

        #NUMBER OF DESTINATIONS
        n = len(tickets)

        result = ["JFK"]
        def dfs(start):
            #ALL TICKETS USED
            if len(result) == n + 1:
                return True

            #NO PATH FROM HERE
            if start not in graph:
                return False

            #ITERATE OVER THE COPY
            temp = graph[start][:]
            for i, v in enumerate(temp):
                #REMOVE FROM LIST AND ADD TO RESULT
                graph[start].pop(i)
                result.append(v)
                if dfs(v):
                    return True
                #NO PATH: ADD TO LIST AND REMOVE FROM RESULT
                graph[start].insert(i, v)
                result.pop()

            return False

        dfs("JFK")
        return result

