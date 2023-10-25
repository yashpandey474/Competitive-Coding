t = int(input())

for i in range(t):
    string = input()
    
    if string == "abc":
        print("YES")
        continue
    
    total = 0
    test = "abc"
    for i in range(3):
        if string[i] != test[i]:
            total += 1
            
    if total <= 2:
        print("YES")
        continue
    
    print("NO")