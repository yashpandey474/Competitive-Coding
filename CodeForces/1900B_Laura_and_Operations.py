t = int(input())
for i in range(t):
    l = list(map(int, input().split()))
    
    lis = ["0", "0", "0"]
    total = sum(l)
    # CHECK FOR ONE'S
    if (total - l[0]) % 2 == 0:
        lis[0] = "1"
            
    if (total - l[2]) % 2 == 0:
        lis[2] = "1"
            
            
    if (total - l[1]) % 2 == 0:
        lis[1] = "1"
            
            
    print(" ".join(lis)) 
        
        
        
        