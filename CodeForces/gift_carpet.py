t = int(input())



def checkVika(arr):
    rows, cols = len(arr), len(arr[0])
    map_vika = {i: set() for i in "vika"}
    
    for i in range(cols):
        for j in range(rows):
            if arr[j][i] in map_vika:
                map_vika[arr[j][i]].add(i)
                
    for i in map_vika:
        if len(map_vika[i]) == 0:
            return "NO"
    
    string = "vika"
    n = 4
    cache = {}
    def dfs(index, column, prevMax):
        if (index, column, prevMax) in cache:
            return cache[(index, column, prevMax)]
        
        if index >= n:
            return True
        
        if column >= cols:
            return False
        
        res = dfs(index, column + 1, prevMax)
        
        if column in map_vika[string[index]] and column > prevMax:
            res = dfs(index + 1, column + 1, column)
            
        cache[(index, column, prevMax)] = res
        return res
    
    res = dfs(0, 0, -1)
    
    return ("YES" if res else "NO")
    
for i in range(t):
    n, m = map(int, input().split())
    
    arr = []
    for j in range(n):
        row = str(input())
        arr.append(row)
        
    print(checkVika(arr))
    
        