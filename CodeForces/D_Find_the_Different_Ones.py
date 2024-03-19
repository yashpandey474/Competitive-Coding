for test in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    
    count = [-1  for i in range(n)]
    
    curr_ele = a[0]
    curr_index = 0
    for i in range(1, n):
        if a[i] != curr_ele:
            count[curr_index] = i
            curr_ele = a[i]
            curr_index = i
        
    if count[0] != -1:    
        for i in range(1, n):
            if count[i] == -1 and count[i - 1] != i:
                count[i] = count[i - 1]
    
    for i in range(q):
        l, r = map(int, input().split())
        
        l, r = l - 1, r - 1
        if count[l] == -1 or r < count[l]:
            print(-1, -1)
            
        else:
            print(l + 1, count[l] + 1)
            
    
        