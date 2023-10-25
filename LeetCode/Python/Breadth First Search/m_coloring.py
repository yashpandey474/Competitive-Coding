#Function to determine if graph can be coloured with at most M colours such
#that no two adjacent vertices of graph are coloured with same colour.


def can_color(vertex, color, colors, graph):
    for i in graph[vertex]:
        if i != vertex and colors[i] == color:
            return False
    return True


def m_coloring(graph, m, start,  v, colors):
    if start == v:
        return True
        
    for color in range(1, m+1):
        if can_color(start, color, colors, graph):
            colors[start] = color
            #BACKTRACKING WITH THIS COLOR
            if m_coloring(graph, m, start+1, v, colors):
                return True
            colors[start] = 0
            
    return False
    
def graphColoring(graph, k, V):
    
    #your code here
    colors = [0]*V
    return m_coloring(graph, k, 0,  V, colors)
