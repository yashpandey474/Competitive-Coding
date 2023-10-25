
def recursion(nums, target, current_sum, answer, result):
    if current_sum == target:
        result.append(answer)
        return
    
    if current_sum > target:
        return
    
    for i in nums:
        recursion(nums, target, current_sum + i, answer + [i], result)

        
def combination_sum(nums, target):
    res = []
    recursion(nums, target, 0, [], res)
    return len(res)
