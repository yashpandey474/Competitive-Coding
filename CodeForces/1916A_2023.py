t = int(input())

for i in range(t):
    n, k = map(int, input().split())
    
    sequence = list(map(int, input().split()))
    
    curr_prod = 1
    for a in sequence:
        curr_prod *= a
        
    # NO SOLUTION
    if 2023 % curr_prod != 0:
        print("NO")
        
    else:
        print("YES")
        
        a = 2023//curr_prod
        print(a, end = " ")
        for j in range(k - 1):
            print(1, end = " ")
            
        print()
                
        