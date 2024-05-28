import math
t = int(input())

for test in range(t):
    n = int(input())

    if n == 2:
        print(2)
        print(2, 1)
        continue

    print(2)

    i = n
    print(i, i - 1)
    prev = i
    i -= 2
    while i > 0:
        print(i, prev)
        prev = math.ceil((i + prev)/2)
        i -= 1

