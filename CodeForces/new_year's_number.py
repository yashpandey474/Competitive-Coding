t = int(input())



for i in range(t):
    n = int(input())
    
    
    if n == 2020 or n == 2021:
        print("YES")
        continue
    
    if n < 2020:
        print("NO")
        continue
        
    i = 0

    while i >= 0:
        value = n - (2020*i)
        
        if value < 0:
            print('NO')
            break
        
        if value % 2021 == 0:
            print("YES")
            break
        
        i += 1
        
    
        
        
    
    
            
    