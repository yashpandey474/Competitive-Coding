t = int(input())

for test in range(t):
    n = int(input())

    r1 = "##.."*(n//2)
    r2 = "..##"*(n//2)
    if n % 2 != 0:
        r1 += "##"
        r2 += ".."

    for i in range(n):
        if i % 2 == 0:
            print(r1)
            print(r1)
        else:
            print(r2)
            print(r2)


