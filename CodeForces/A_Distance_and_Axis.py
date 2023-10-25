t = int(input())
for i in range(t):
    a, k = map(int, input().split())

    if k > a:
        print(k - a)
        
    else:
        if ((a-k)&1):
            print(1)
            
        else:
            print(0)
