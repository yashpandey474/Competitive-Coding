t = int(input())

for test in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    if len(set(a)) == 1:
        print("YES")
        continue

    total = sum(a)

    flag = 0
    for i in a:
        if total == i*n:
            print("YES")
            flag = 1
            break

    if not flag:
        print("NO")
            
    