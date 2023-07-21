def can_reach_final_milestone(milestones: list[int]) -> bool: 
    max_possible = 0
    print(milestones)
    for i in range(len(milestones)):
        if i > max_possible:
            return False
            
        max_possible = max(max_possible,  i + milestones[i])
            
    return True
