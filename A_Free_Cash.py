n = int(input())

count = 1
max_count = 1

prev_h, prev_m = -1, -1

for i in range(n):
    h, m = map(int, input().split())

    if h == prev_h and m == prev_m:
        count += 1
        max_count = max(max_count, count)

    else:
        count = 1

    prev_h, prev_m = h, m

print(max_count)
