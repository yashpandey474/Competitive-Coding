t = int(input())

for i in range(t):
    n = int(input())
    
    a = list(map(int, input().split()))
    
    # APPLY OPERATION ANY NUMBER OF TIMES
    
    # SELECT AN INDEX I AND AN INTEGER X
    # SET Ai = (Ai xor X) and Ai+1 = (Ai+1 xor X)
    # CAN MAKE ALL ELEMENTS EQUAL OR NOT?
    
    if n%2 != 0:
        print("YES")
        continue
    
    # OVERALL XOR OF ARRAY DOESN'T CHANGE
    s = 0
    for ele in a:
        s = s^ele
        
    # IF n IS EVEN: ONLY IF S = 0
    if s == 0:
        print("YES")
        continue
    
    print("NO")
    
    
    
    