#IDEA: FOR EACH DIGIT, CHECK IF THE OPPOSITE DIGIT IS PRESENT UNTIL COUNT OF ONE OF THE DIGITS REACHES -1
t = int(input())
for j in range(t):
    s = str(input())
    
    count_0s = 0
    count_1s = 0
    
    for a in s:
        if a == "0":
            count_0s +=1
        else:
            count_1s += 1
    
    flag = False
    for i in range(0, len(s), 1):
        if s[i] == "0":
            if count_1s == 0:
                flag = True
                break
            count_1s -= 1
            
        else:
            if count_0s == 0:
                flag = True
                break
            count_0s -= 1
            
    if not flag:
        print(0)
        
    else:
        print(len(s) - i)
    
            
            