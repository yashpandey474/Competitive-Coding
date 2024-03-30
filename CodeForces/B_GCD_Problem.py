t = int(input())

for test in range(t):
    n = int(input())
    
    if n % 2 == 0:
        print(2, n - 3, 1)

    else:
        if n % 4 == 1:
            print(n // 2 - 1, n // 2 + 1, 1)

        else:
            print(n // 2 - 2, n // 2 + 2, 1)
        