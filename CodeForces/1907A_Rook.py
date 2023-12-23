t = int(input())

for i in range(t):
    s = str(input())
    col = s[0]
    row = int(s[1])
    
    for i in range(1, 9):
        if i != row:
            print(col + str(i))
            
    for i in range(ord("a"), ord("i")):
        if chr(i) != col:
            print(chr(i) + str(row))
            
    