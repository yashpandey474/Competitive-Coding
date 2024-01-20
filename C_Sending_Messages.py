t = int(input())
for i in range(t):
    n, f, a, b = map(int, input().split())
    moments = list(map(int, input().split()))
    moments = [0] + moments
    
    j = 0
    flag = False
    while j < n:
        diff = moments[j + 1] - moments[j]
        c1 = a*diff
        if c1 > b:
            c1 = b 
            
        if c1 >= f:
            print("NO")
            flag = True
            break
        
        f -= c1
        j += 1
        
    if not flag:
        print("YES")
                
            
            