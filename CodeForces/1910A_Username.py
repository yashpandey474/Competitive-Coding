t = int(input())

for j in range(t):
    s = str(input())
    
    for i in range(len(s) - 1, -1, -1):
        if s[i] >= "0" and s[i] <= "9":
            if s[i] != "0":
                print(s[: i])
                break