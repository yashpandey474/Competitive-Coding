t = int(input())

a = list(map(int, input().split()))

for i in a:
    if i > 14 and 7 > i % 14 > 0:
        print("YES")

    else:
        print("NO")
        continue

