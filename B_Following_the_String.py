t = int(input())

for test in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    s = "" 
    chars = [0 for i in range(26)]

    for i in range(n):
        for j in range(26):
            if chars[j] == a[i]:
                chars[j] += 1
                s += chr(ord('a') + j)
                break
                
    print(s)