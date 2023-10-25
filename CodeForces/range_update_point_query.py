t = int(input())


def sumDigits(number):
    total = 0
    
    while number > 0:
        total += number % 10
        number = number // 10
        
    return total
for i in range(t):
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))
    
    for j in range(q):
        string = input().split()
        
        left, right, x = -1, -1, -1
        
        if string[0] == "1":
            left = int(string[1])
            right = int(string[2])
            
        else:
            x = int(string[2])
            
            
        if x != -1:
            print(arr[x - 1])
            continue
        
        for k in range(left - 1, right):
            arr[k] = sumDigits(arr[k])
            
