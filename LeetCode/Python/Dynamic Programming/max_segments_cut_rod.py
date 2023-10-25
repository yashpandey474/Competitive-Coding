def cutSegments(n, x, y, z):
    # Write your code here.
    

    cache = {}

    def dfs(length):
        if length == 0:
            return 0

        if length in cache:
            return cache[length]


        res = -float('inf')

        if length >= x:
            res = max(res, 1 + dfs(length - x))

        if length >= y:
            res = max(res, 1 + dfs(length - y))

        if length >= z:
            res = max(res, 1 + dfs(length - z))


        cache[length] = res
        return res

    res = dfs(n)
    return (0 if res == -float('inf') else res)
