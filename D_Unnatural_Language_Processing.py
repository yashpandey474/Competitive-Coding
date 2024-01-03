t = int(input())
string = ""

def dfs(s, index):
    global string
    if index >= len(s):
        string = s
        return True
    
    if index == len(s) - 1:
        return False
    
    
    if s[index] in "bcd" and s[index + 1] in "ae":
        if dfs(s[index: index + 2] + "." + s[index + 2: ], index + 2):
            return True
        
        if index < len(s) - 2:
            if s[index + 2] in "bcd":
                if dfs(s[index: index + 3] + "." + s[index + 3: ], index + 3):
                    return True
                
    return False

for i in range(t):
    
    n = int(input())
    
    s = str(input())
    
    # CV or CVC
    dfs(s, 0)
    print(string)
    