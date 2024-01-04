t = int(input())
string = ""

for i in range(t):
    
    n = int(input())
    
    s = str(input())
    
    set1 = set()
    
    set1.add("a")
    set1.add("e")

    # TRAVERSE FROM RIGHT TO LEFT
    j = len(s) - 1
    while j > 0:
        # print("CHAR = ", s[j], "J = ", j)
        # IF CHARACTER IS A VOWEL, MUST BE PART OF A "CV"
        if s[j] in set1:
            s = s[ : j - 1] + "." + s[j - 1: j + 1] + s[j + 1: ]
            j = j - 2
            
        elif s[j] in "bcd":
            s = s[ : j - 2] + "." + s[j - 2: j + 1] + s[j + 1: ]
            j = j - 3
            
        # print("STRING = ", s)
            
    print(s[1: ])
        
    