t = int(input())

for test in range(t):
    n = int(input())
    s = str(input())

    # if n % 2 != 0:
    #     if len(set(s)) <= 2:
            

    for i in range(1, n + 1):
        flag1 = 0
        flag2 = 0

        if n % i != 0:
            continue

        for j in range(n):
            b = - (j % i) + i
            if s[j] != s[j % i]:
                flag1 += 1

            if s[j] != s[-b]:
                flag2 += 1

            if flag1 > 1 and flag2 > 1:
                break

        if flag1 < 2 or flag2 < 2:
            break

    print(i)
            
                
    

