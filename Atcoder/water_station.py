n = int(input())

x = abs(n - (n//5)*5)
y = abs(n - (n//5 + 1)*5)

if x <= y:
    print((n//5)*5)
    
else:
    print((n//5 + 1)*5)