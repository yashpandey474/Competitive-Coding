// User function Template for Java
class Edge{
        int u;
        int wt;
        
        Edge(int u, int wt){
            this.u = u;
            this.wt = wt;
        }
    }
class sortByWt implements Comparator<Edge>{
        public int compare(Edge e1, Edge e2){
            return e1.wt - e2.wt;
        }
    }
class Solution{
    
    
    
	static int spanningTree(int V, int E, int edges[][]){
	    // Code Here. 
	    if (V == 0){
	        return 0;
	    }
	    
	    //VISITED ARRAY
	    int[] visited = new int[V];
	    //MARK ALL AS UNVISITED
	    Arrays.fill(visited, 0);
	    
	    
	    //PRIORITY QUEUE
	    PriorityQueue<Edge> q = new PriorityQueue<>(new sortByWt());
	    //NODE AND WEIGHT
	    q.add(new Edge(0, 0));
	    
	    int total_sum = 0;
	    
	    //PRIM'S ALGORITHM
	    while (!q.isEmpty()){
	        Edge e = q.poll();
	        
	        //CHECK IF NODE IS VISITED
	        if (visited[e.u] == 1){
	            continue;
	        }
	        
	        //MARK NODE AS VISITED
	        visited[e.u] = 1;
	        //ADD EDGE WEIGHT
	        total_sum += e.wt;
	        
	        //STORE UNVISITED NEIGHBOUR EDGES
	        for (int i = 0; i<edges.length; i++){
	            if (edges[i][0] == e.u){
	                int neighbor = edges[i][1];
	                int weight = edges[i][2];
	                
	                if (visited[neighbor] == 0){
	                    q.add(new Edge(neighbor, weight));
	                }
	            }
	            else if (edges[i][1] == e.u){
	                int neighbor = edges[i][0];
	                int weight = edges[i][2];
	                
	                if (visited[neighbor] == 0){
	                    q.add(new Edge(neighbor, weight));
	                }
	            }
	        }
	    }
	    
	    return total_sum;
	    
	}
}
