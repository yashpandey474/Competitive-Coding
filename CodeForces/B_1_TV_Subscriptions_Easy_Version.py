t = int(input())

for test in range(t):
    n, k, d = map(int, input().split())

    a = list(map(int, input().split()))

    diff = {}

    min_count = float('inf')

    for i in range(n):
        if a[i] not in diff:
            diff[a[i]] = 0

        diff[a[i]] += 1

        if i == d - 1:
            min_count = min(min_count, len(diff))

        elif i  >= d:
            diff[a[i - d]] -= 1

            if diff[a[i - d]] == 0:
                del diff[a[i - d]]

        
            min_count = min(min_count, len(diff))

    print(min_count)