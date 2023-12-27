t = int(input())

for j in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    #TAKE THE MAXIMUM OF EACH STREAM OF SAME SIGN NUMBERS
    total = 0
    curr = arr[0]
    i = 0
    
    while i < n:
        if arr[i]*curr > 0:
            while i < n and arr[i]*curr > 0:
                curr = max(curr, arr[i])
                i += 1
                
            total += curr
            
            if i < n:
                curr = arr[i]
        else:
            i += 1
            total += curr
            curr = arr[i]
            
     
    print(total)