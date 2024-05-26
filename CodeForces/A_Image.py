t = int(input())

for test in range(t):
    r1 = list(str(input()))
    r2 = list(str(input()))

    r1 = set(r1 + r2)

    print(len(r1) - 1)

