t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    numPos, numNeg, numZero = 0, 0, 0
    for ele in a:
        if ele == 0:
            numZero += 1
        if ele < 0:
            numNeg += 1
            
        elif ele > 0:
            numPos += 1
    
    # PRODUCT IS NOT ZERO   
    if numZero == 0:
        
        # NO NEGATIVE NUMBERS [ALL POSITIVE]
        if numNeg == 0:
            print(1)
            print(1, 0)
        
        else:
            # ODD NUMBER OF NEGATIVE NUMBERS
            if numNeg % 2 != 0:
                print(0)
            
            # EVEN NUMBER OF NEGATIVE NUMBERS
            else:
                i = 0
                for j in range(n):
                    if a[j] < 0:
                        print(1)
                        print(1+j, 0)
                        break
                
    
    # PRODUCT IS ZERO  
    else:
        print(0)
        