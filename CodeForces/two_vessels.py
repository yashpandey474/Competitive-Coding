t = int(input())

for i in range(t):
    a, b, c = map(int, input().split())

    target = (a + b)/2

    if a < b:
        res = (target - a)/c
        
        # print("RES = ", res)
        if res > int((target - a)//c):
            print(int(res + 1))
            
        else:
            print(int(res))
        
    else:
        res = (target - b)/c
        # print("RES = ", res)
        if res > int((target - b)//c):
            print(int(res + 1))
        else:
            print(int(res))