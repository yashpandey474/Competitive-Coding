n = int(input())
s = str(input())

num_Os = 0
num_Ls = 0


taken_Os = 0
taken_Ls = 0

for i in range(len(s)):
    if s[i] == "O":
        num_Os += 1
    else:
        num_Ls += 1
        
flag = False
for i in range(len(s) - 1):
    if s[i] == "O":
        taken_Os += 1
        num_Os -= 1
        
    else:
        taken_Ls += 1
        num_Ls -= 1
        
    if num_Ls != taken_Ls and num_Os != taken_Os:
        print(i + 1)
        flag = True
        break
    
if not flag:
    print (-1)
    
        
    