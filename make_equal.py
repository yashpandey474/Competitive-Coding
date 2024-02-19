t = int(input())

for test in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    count = sum(a)//n
    
    a = [count - ele for ele in a]
    curr_sum = 0
    flag = False
    for  i in range(n - 1, -1, -1):
        curr_sum += a[i]
        
        if curr_sum < 0:
            flag = True
            print("NO")
            break
    
    if not flag:
        print("YES")
        
    