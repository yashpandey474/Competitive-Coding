t = int(input())
arr = []
max_sum = -float('inf')

def dfs(index, current):
    global max_sum
    if index >= n - 1:
        max_sum = max(max_sum, current)
        return
    
    dfs(index + 1, current)
    if arr[index]*arr[index + 1] < 0 or arr[index] < 0:
        current -= arr[index] + arr[index + 1]
        
        arr[index] = -arr[index]
        arr[index + 1] = -arr[index + 1]
        
        current += arr[index] + arr[index + 1]

        dfs(index + 1, current)
        
        current -= arr[index] + arr[index + 1]

        arr[index] = -arr[index]
        arr[index + 1] = -arr[index + 1]

        current += arr[index] + arr[index + 1]  
    
    
for i in range(t):

    n = int(input())
    arr = list(map(int, input().split()))
    max_sum = -float('inf')
    
    dfs(0, sum(arr))
    print(max_sum)
    