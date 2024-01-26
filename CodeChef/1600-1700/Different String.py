t = int(input())

for i in range(t):
    # SOLUTION ALWAYS EXISTS. NUMBER OF STRINGS OF LENGTH N => pow(2, N) 
    n = int(input())
    xor = 0
    string_set = set()
    for j in range(n):
        s = str(input())
        string_set.add(int(s, 2))
        
    for j in range(pow(2, n)):
        if j not in string_set:
            string = bin(j)[2:]
            string = "0"*(n - len(string)) + string
            print(string)
            break