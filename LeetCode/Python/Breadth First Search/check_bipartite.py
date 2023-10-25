class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        visited = set()
        color_vertices = {}

        #GRAPH MAY BE UNCONNECTED: ITERATE OVER ALL 
        for start in range(len(graph)):
            #ALREADY COVERED IN ANOTHER COMPONENT
            if start in visited:
                continue
            queue = [start]
            color_vertices[start] = 1
            
            while queue:
                current = queue.pop(0)

                for i in graph[current]:
                    if i in color_vertices and color_vertices[i] == color_vertices[current]:
                        return False
                    if i not in visited:
                        visited.add(i)
                        color_vertices[i] = -color_vertices[current]
                        queue.append(i)

        return True


