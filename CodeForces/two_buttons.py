n, m = map(int, input().split())

#MULTIPLY BY 2 OR SUBTRACT 1

cache = {}

print("N = ", n, "M = ", m)
def dfs(number):
    
    if number == m:
        return 0    
    
    if number <= 0:
        return float('inf')
    
    if number in cache:
        return cache[number]
    
    if number > m:
        return number - m


    res = min(
            dfs(number * 2) + 1,
            dfs(number - 1) + 1
    )
    
    cache[number] = res
    
    return res
print(dfs(n))