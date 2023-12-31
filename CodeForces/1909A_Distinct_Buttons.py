t = int(input())

for i in range(t):
    n = int(input())
    
    points = []
    
    negx, posx, negy, posy = False, False, False, False
    for j in range(n):
        x, y = map(int, input().split())
        if x > 0:
            posx = True
        
        if x < 0:
            negx = True
            
        if y > 0:
            posy = True
            
        if y < 0:
            negy = True
            
    if negx and posx and negy and posy:
        print("NO")
        
    else:
        print("YES")
        
    #CAN REACH ALL THE POINTS OR NOT