# x = (q - p)/2
# y = (q + p)/2

t = int(input())

for test in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    m = int(input())
    q = list(map(int, input().split()))

    odd_p = 0
    odd_q = 0

    for i in p:
        if i % 2 == 1:
            odd_p += 1
    for i in q:
        if i % 2 == 1:
            odd_q += 1
    
    print(odd_p * odd_q + (n - odd_p) * (m - odd_q))