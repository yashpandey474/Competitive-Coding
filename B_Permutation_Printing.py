t = int(input())

for test in range(t):
    n = int(input())

    count = [i for i in range(1, n + 1)]
    a = []
    
    i = 0
    while len(a) < n:
        a.append(count[i])
        
        if len(a) >= n:
            break
        a.append(count[n - i- 1])
        i += 1
    print(" ".join(map(str, a)))
