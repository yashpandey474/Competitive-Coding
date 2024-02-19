t = int(input())

for test in range(t):
    n = int(input())
    
    string = ""
    
    for i in range(3):
        res = max(1, n - (3 - 1 - i)*26)
            
        string += chr(res - 1 + ord('a'))
        n -= (res)
    print(string)
    