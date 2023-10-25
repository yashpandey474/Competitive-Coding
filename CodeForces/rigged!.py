t = int(input())
strength, endurance, n = [], [], 0


def canWin(mid):

    if mid > strength[0]:
        return False

    current = endurance[0]

    for i in range(1, n):
        if strength[i] < mid:
            continue

        if endurance[i] >= current:
            return False

    return True


for i in range(t):
    n = int(input())

    strength = []
    endurance = []
    for i in range(n):
        s, e = map(int, input().split())
        strength.append(s)
        endurance.append(e)

    l = 1
    r = strength[0]

    if canWin(r):
        print(r)
        continue
    
    print(-1)
    # found = False
    # for i in range(l, r + 1):
    #     if canWin(i):
    #         print(i)
    #         found = True
    #         break

    # if not found:
    #     print(-1)
