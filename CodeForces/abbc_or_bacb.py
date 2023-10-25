t = int(input())
n, s = 0, []

cache = {}
def dfs(index):
    global n
    global s
    if (index, tuple(s)) in cache:
        return cache[(index, tuple(s))]
    
    if index >= n - 1:
        return 0
     
    res = dfs(index + 1)
    
    if s[index: index + 2] == ["A", "B"]:
        s[index: index + 2] = ["B", "C"]
        
        if index > 0:
            res = max(
                res,
                1 + dfs(index - 1),
            )
            
        else:
            res = max(
                res,
                1 + dfs(index + 2)
            )
            
        s[index: index + 2] = ["A", "B"]
        
    if s[index: index + 2] == ["B", "A"]:
        s[index: index + 2] = ["C", "B"]
        res = max(
            res,
            1 + dfs(index + 1)
        )
        s[index: index + 2] = ["B", "A"]
        
    cache[(index, tuple(s))] = res
    
    return res

for i in range(t):
    s = list(input())
    
    n = len(s)

    
    # print("N = ", n, "S = ", s)
    print(dfs(0))
    
