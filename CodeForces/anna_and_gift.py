t = int(input())
import heapq
for test in range(t):
    
    print("\n\n TEST CASE", test)
    n, m = map(int, input().split())
    r = list(map(int, input().split()))
    
    r = sorted(r, reverse = True)
    
    cache = {}
    def dfs(arr, index, turn):
        if index > n:
            return sum(arr)
        
        if (tuple(arr), index, turn) in cache:
            return cache[(tuple(arr), index, turn)]
        
        res = dfs(arr, index + 1, turn)
        store = r[index]
        if turn == 0:
            r[index] = int(str(r[index])[::-1])
            r = sorted(r, reverse = True)
            res = max(res, dfs(arr,index + 1, 1))
            
        elif turn == 1:
            if len(arr) == 1:
                return arr[0]
            
            r[index]
            
            
            
            