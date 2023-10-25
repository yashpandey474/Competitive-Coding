def floydWarshall(n, m, src, dest, edges):
    # Write your code here.

    #DP FOR ALL MINIMUM DISTANCES
    dp = [[float('inf') for i in range(n+1)] for _ in range(n+1)]

    #SAME VERTEX
    for i in range(n):
        dp[i][i] = 0

    #ADD ALL EDGES TO MATRIX
    for edge in edges:
        dp[edge[0]][edge[1]] = edge[2]

    #ITERATE OVER N^3
    for i in range(1, n+1):
        for j in range(1, n+1):
            for k in range(1, n+1):
                if dp[i][k] != float('inf') and dp[k][j] != float('inf'):
                    dp[i][j] = min(
                        dp[i][j],
                        dp[i][k] + dp[k][j]
                    )


    #RETURN FOR SOURCE TO DESTINATION
    if dp[src][dest] == float('inf'):
        return 1000000000
        
    return dp[src][dest]
