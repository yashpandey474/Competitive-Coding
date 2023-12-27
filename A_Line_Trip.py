t = int(input())
for i in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    
    a = [0,] + a + [x, ]
    
    b = []
    
    for j in range(len(a) - 1):
        if j == len(a) - 2:
            b.append(2*(a[j + 1] - a[j]))
            
        else:
            b.append(a[j + 1] - a[j])
            
    print(max(b))
            
         
    
    