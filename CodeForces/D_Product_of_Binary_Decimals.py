a = set([1, 10, 11, 100, 101, 110, 111])
for i in range(112, 100001):
    if all(digit in {"0", "1"} for digit in str(i)):
        a.add(i)
        continue

    for j in a:
        if j > i:
            break
        if i % j == 0 and i//j in a:
            a.add(i)
            break
t = int(input())
for test in range(t):
    n = int(input())

    res = n in a

    print("YES" if res == 1 else "NO")
        
