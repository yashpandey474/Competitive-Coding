te = int(input())

for test in range(te):
    s = str(input())
    a = 0
    b = 0
    
    for e in s:
        if e == "A":
            a += 1
            
        else:
            b += 1
            
    if a > b:
        print("A")
    else:
        print("B")
    