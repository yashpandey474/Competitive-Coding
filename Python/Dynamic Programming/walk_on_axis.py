# cook your dish here
t = int(input())


def dfs(start, end, current):
    if start > end:
        return 0
        
    # print("START = ", start, "END = ", end, "CURRENT = ", current)
        
    if current == "E":
        return end - start + dfs(start, end - 1, "S")
        
    else:
        return end - start + dfs(start + 1, end, "E")
        
    
        
for i in range(t):
    n = int(input())
    
    print(n + dfs(0, n, "E"))
