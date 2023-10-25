n, k = map(int, input().split())
arr = list(map(int, input().split()))

st = 0
en = k 
current = sum(arr[st:en])
min_sum = current
index = st + 1

while en < n:
    current += arr[en]
    current -= arr[st]
    
    en += 1
    st += 1
    
    if current < min_sum:
        min_sum = current
        index = st + 1
    
    
    
print(index)