t = int(input())

for test in range(t):
    n = int(input())
    flag = False
    for a in range(n):
        s = str(input())
        
        count = 0
        for ele in s:
            if ele == "1":
                count += 1
                
        if count == 1:
            flag = True
            

    if not flag:
        print("SQUARE")
        
    else:
        print("TRIANGLE")