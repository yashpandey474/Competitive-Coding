t = int(input())

for test in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    for i in range(n):
        if a[i] != 0:
            break
    
    if i == n - 1:
        print(0)
        continue

    count = 0

    while i < n - 1:
        if a[i] == 0:
            count += 1

        else:
            count += a[i]

        i += 1

    print(count)