t = int(input())

for test in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort()

    flag = 0
    for i, ele in enumerate(a):
        if ele == b[i]:
            continue
        
        elif ele < b[i] and b[i] - ele == 1:
            continue

        else:
            flag = 1
            print("NO")
            break

    if not flag:
        print("YES")
    