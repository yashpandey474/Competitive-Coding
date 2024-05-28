t = int(input())

for test in range(t):
    n, m = map(int, input().split())

    if n % 2 != m % 2:
        print("Burenka")

    else:
        print("Tonya")