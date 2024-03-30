t = int(input())

for test in range(t):
    n = int(input())
    x = list(map(int, input().split()))

    if x[- 1] - x[0] <= n + 1:
        print("YES")

    else:
        print("NO")