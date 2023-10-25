from typing import List

def generateString(N: int) -> List[str]:
    # write your code here

    res = []

    #DFS FUNCTION
    def dfs(length, prev, string):

        if length == N:
            res.append(string)
            return

        if prev == 0:
            dfs(length + 1, 1, string + "1")
            dfs(length + 1, 0, string + "0")

        else:
            dfs(length + 1, 0, string + "0")


    dfs(1, 0, "0")
    dfs(1, 1, "1")
    return res
