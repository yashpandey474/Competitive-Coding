t = int(input())

for test in range(t):
    a, b, c, d = map(int, input().split())

    r = max(a*d, b*c)
    h = min(a*d, b*c)

    
    if r == h:
        print(0)
    elif h == 0  or r % h == 0:
        print(1)

    else:
        print(2)