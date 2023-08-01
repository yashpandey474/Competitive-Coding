def countStrings(n):
    # Write your code here.
    
    cache = {}

    def dfs(length, b, c):
        if b > 1 or c > 2:
            cache[(length, b, c)] = 0
            return 0

        if length == n:
            return 1

        if (length, b, c) in cache:
            return cache[(length, b, c)]

        res = 0
        res += (
            dfs(length + 1, b, c) + 
            dfs(length + 1, b + 1, c) + 
            dfs(length + 1, b, c + 1)
        )

        cache[(length, b, c)] = res
        return (res%(10**9 + 7))
    return dfs(0, 0, 0)
