t = int(input())
stones = []

def dfs(left, right, min_done, max_done):
    if (left, right, min_done, max_done) in cache:
        return cache[(left, right, min_done, max_done)]

    if left > right:
        return 0

    if min_done and max_done:
        return 0

    res = float('inf')
    left_min, left_max = min_done, max_done
    right_min, right_max = min_done, max_done

    if stones[left] == min_val:
        left_min = True

    if stones[left] == max_val:
        left_max = True

    if stones[right] == min_val:
        right_min = True

    if stones[right] == max_val:
        right_max = True

    res = min(
            1 + dfs(left + 1, right, left_min, left_max),
            1 + dfs(left, right - 1, right_min, right_max)
        )

    cache[(left, right, min_done, max_done)] = res
    return res


for i in range(t):
    n = int(input())
    stones = list(map(int, input().split()))
    max_val = max(stones)
    min_val = min(stones)
    cache = {}
    
    print(dfs(0, n - 1, False, False))