def minCost(cost):
    # Write your code here.
    
    #CACHE
    cache = {} #INDEX, PREVIOUS

    #DEPTH FIRST SEARCH FUNCTION
    def dfs(index, previous):
        #ALL PROCESSED
        if index >= len(cost):
            return 0

        #ALREADY IN CACHE
        if (index, previous) in cache:
            return cache[(index, previous)]

        #PROCESS
        res = float('inf')

        for i in range(3):
            if previous != i:
                res = min(
                    res,
                    dfs(index + 1, i) + cost[index][i]
                )

        cache[(index, previous)] = res
        return res
    
    return dfs(0, -1)
