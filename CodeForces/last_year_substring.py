t = int(input())

n = 0
s = ""
def dfs(index, string, jump):
    global n
    global s
    if index >= n:
        return string == "2020"

    if string == "2020":
        return not jump

    res = dfs(index + 1, string, jump)

    if not jump:
        if string == "2" and s[index] != "0":
            res = res or dfs(index + 1, string, True)

        if string == "20" and s[index] != "2":

            res = res or dfs(index + 1, string, True)

        if string == "202" and s[index] != "0":

            res = res or dfs(index + 1, string, True)

        if string == "" and s[index] != "2":


            res = res or dfs(index + 1, string, True)
    
    return res
for i in range(t):
    n = int(input())
    s = input()

    if s == "2020":
        print("YES")
        continue

    