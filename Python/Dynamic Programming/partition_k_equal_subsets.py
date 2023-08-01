from sys import stdin, stdout, setrecursionlimit
setrecursionlimit(10 ** 7)

def canPartitionKSubsets(arr, n, k):
    # Write your code here.
    #TOTAL SUM OF ARRAY
    total_sum = sum(arr)

    #NOT POSSIBLE TO DIVIDE
    if total_sum % k != 0:
        return False

    #TARGET SUM OF EACH SUBSET
    target_sum = sum(arr)//k
    cache = {}
    used = [False]*n

    def dfs(index, subsets, current):
        if subsets == 0:
            return True

        if index >= len(arr):
            if current == target_sum:
                return dfs(0, subsets - 1, 0)
            return False

        if (index, subsets, current) in cache:
            return cache[(index, subsets, current)]

        if current > target_sum:
            return False

        res = dfs(index + 1, subsets, current)

        if not used[index]:
            used[index] = True
            res = res or dfs(index + 1, subsets, current + arr[index])
            used[index] = False

        cache[(index, subsets, current)] = res
        return res

    return dfs(0, k, 0)

