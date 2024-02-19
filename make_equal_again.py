t = int(input())

for test in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    i = 0
    j = n - 1
    x = a[0]
    min_cost = float('inf')
    flag = False
    while i <= j:
        # print(a[i], a[j])
        if a[i] == a[j] == x:
            i += 1
            j -= 1
            
        elif a[i] == x:
            i += 1
            
        elif a[j] == x:
            j -= 1
        
        else:
            flag = True
            min_cost = min(min_cost, j - i + 1)
            break
        
    if n > 2 and a[0] != a[n - 1]: 
        x = a[n - 1]
        i = 0
        j = n - 1
        while i <= j:
            # print(a[i], a[j])
            if a[i] == a[j] == x:
                i += 1
                j -= 1
                
            elif a[i] == x:
                i += 1
                
            elif a[j] == x:
                j -= 1
            
            else:
                flag = True
                min_cost = min(min_cost, j - i + 1)
                break
            
            
    if not flag:
        print(0)
    
    else:
        print(min_cost)
            