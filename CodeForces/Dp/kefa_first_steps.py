n = int(input())
arr = list(map(int, input().split()))

i = 0
j = 1

max_len = 1
while j < n:
    if arr[j] >= arr[j - 1]:
        j += 1
    
    else:
        max_len = max(max_len, j - i)
        i = j
        j += 1
        
max_len = max(max_len, j - i)
    
      
print(max_len)