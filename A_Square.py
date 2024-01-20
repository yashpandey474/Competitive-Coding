t = int(input())
for i in range(t):
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split()) 
    x4, y4 = map(int, input().split())
    
    a = min(x1, x2, x3, x4)
    b = max(x1, x2, x4, x3)
    
    print((a-b)**2)