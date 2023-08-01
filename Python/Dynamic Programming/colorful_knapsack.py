def colorfulKnapsack(w, c, m, x) :
    # Your code goes here
    # Return a single integer
    
    cache = {}
    used = [False]*m

    def dfs(color, weight):
        if weight > x:
            return float('inf')

        if color > m:
            return x - weight

        res = float('inf')
        for i in range(len(w)):
            if c[i] == color:
                res = min(
                    res,
                    dfs(color + 1, weight + w[i])
                )
        cache[(color, weight)] = res
        return res

    result =  dfs(1, 0)
    if result == float('inf'):
        return -1

    return result
    
