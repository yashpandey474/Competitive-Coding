t = int(input())

for test in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    count = []
    
    for i, ele in enumerate(a):
        count.append(i + ele + 1)
        
    b = set()
    count = sorted(count, reverse=True)
    for i in range(n):
            
        while count[i] in b:
            count[i] -= 1
            
        b.add(count[i])

    count = sorted(count, reverse=True)
              
    print(" ".join(map(str, count)))