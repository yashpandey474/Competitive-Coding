t = int(input())
import heapq

cache = {}
def dfs(a, b, index, used, curr_sum):
    if index >= len(a):
        return curr_sum
    
    if (index, tuple(used)) in cache:
        return cache[(index, tuple(used))]
    
    res = 0
    for i in range(len(b)):
        if i not in used:
            used.add(i)
            res = max(res,  dfs(a, b, index + 1, used, curr_sum + abs(a[index] - b[i])))
            used.remove(i)
    cache[(index, tuple(used))] = res
    return res
            
            
for t1 in range(t):
    cache = {}
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    print(dfs(a, b, 0, set(), 0))
    
        