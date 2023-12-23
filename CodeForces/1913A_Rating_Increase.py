#NO OF TESTCASES
t = int(input())

#FOR EACH TESTCASE
for i in range(t):
    ab = str(input())
    flag = False
    
    for j in range(1, len(ab)):
        a = int(ab[: j])
        b = int(ab[j: ])
        
        if str(b) != ab[j: ]:
            continue
        
        if b <= a:
            continue
        
        flag = True
        print(a, b)
        break
    
    if not flag:
        print (-1)
        
        
