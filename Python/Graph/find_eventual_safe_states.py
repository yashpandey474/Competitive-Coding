class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        #STORE TERMINAL AND SAFE NODES
        result = []
        map_safe = {}

        def dfs(start):
            #IF REACHED UNSAFE VISITED NODE
            if start in map_safe:
                return map_safe[start]

            #SET DEFAULT VALUE
            map_safe[start] = False
            for i in graph[start]:
                #IF CAN REACH AN UNSAFE NODE 
                if not dfs(i):
                    break
            else:
                #REMOVE FROM VISITED
                map_safe[start] = True

            #RETURN COMPUTED VALUE
            return map_safe[start]
        
        for i in range(n):
            if dfs(i):
                result.append(i)
        return result

        


        #ADD NODES WHO LEAD TO THESE SAFE NODES ONLY
        
