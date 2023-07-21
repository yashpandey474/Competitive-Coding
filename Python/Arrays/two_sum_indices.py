def find_indices(nums: list[int], target: int) -> list[int]:
    sum_map = {}
    for i in range(len(nums)):
        needed = target - nums[i]
        if needed in sum_map:
            return [sum_map[needed], i]
            
        if nums[i] not in sum_map:
            sum_map[nums[i]] = i
            
    return []
