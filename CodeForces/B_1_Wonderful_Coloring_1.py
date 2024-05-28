t = int(input())

for test in range(t):
    s = str(input())

    n = len(s)

    map1 = {}

    for a in s:
        if a not in map1:
            map1[a] = 0

        map1[a] += 1

    a1 = 0
    a2 = 0

    for a, b in map1.items():
        if b == 1:
            a1 += 1

        else:
            a2 += 1
    print(a2 + a1 // 2)