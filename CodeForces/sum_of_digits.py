m, s = map(int, input().split())


max_number = -float('inf')
min_number = float('inf')

# print("M =", m, "S = ",  s)
def dfs(length, number, current):
    global max_number
    global min_number
    if length >= m:

        # print("NUMBER = ", number)
        if current == s:
            max_number = max(max_number, int(number))
            min_number = min(min_number, int(number))

        return

    if current > s:
        return

    for i in range(10):
        if i == 0 and length == 0:
            continue

        if i + current <= s:
            dfs(length + 1, number + str(i), current + i)
dfs(0, "0", 0)


if max_number == -float('inf'):
    max_number = -1

if min_number == float('inf'):
    min_number = -1
print(min_number, max_number)


