t = int(input())

for test in range(t):
    n = int(input())
    s = input()

    # ZERO LOSSES => DRAW OR WIN EACH GAME
    # WIN AT LEAST ONE => ONE WIN AND REMAINING DRAW OR LOSS



    count2 = 0
    count1 = 0
    map1 = {}
    map2 = {}
    prev = -1
    first = -1

    for i in range(n):
        if s[i] == "1":
            count1 += 1

        else:
            if first == -1:
                first = i

            count2 += 1
            if prev != -1:
                map1[prev] = i
                map2[i] = prev
            prev = i

    if prev != first:
        map1[prev] = first
        map2[first] = prev
    

    if count2 == 0:
        print("YES")
        for i in range(n):
            print("="*i + "X" + "="*(n-i-1))
    
    else:
        if count2 > 2:
            print("YES")
            for i in range(n):
                if s[i] == "1":
                    print("="*i + "X" + "="*(n-i-1))

                else:
                    for j in range(n):
                        if j == i:
                            print("X", end = "")
                        elif j == map1[i]:
                            print("+", end = "")

                        elif j == map2[i]:
                            print("-", end = "")
                        else:
                            print("=", end = "")
                    print()
        else:
            print("NO")
