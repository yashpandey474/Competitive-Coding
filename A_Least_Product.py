t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    flag1, flag2, flag3 = False, False, False
    
    for ele in a:
        if ele == 0:
            flag3 = True
        if ele < 0:
            flag1 = True
            
        elif ele > 0:
            flag2 = True
            
    if not flag3:
        if not flag1:
            print(1)
            print(1, 0)
            
        elif not flag2:
            #EVEN NUMBER OF ELEMENTS
            if len(a) % 2 == 0:
                #CHANGE ONE TO 0
                print(1)
                print(1, 0)
                
            else:
                print(0) 
                
        else:
            print(0)
        
    else:
        print(0)
        