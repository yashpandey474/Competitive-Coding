def longest_common_prefix(strs: list[str]) -> str:
    
    
    prefix = ""
    if (len(strs) == 0):
        return prefix
    
    min_len = min([len(s) for s in strs])
    
    for i in range(min_len):
        for j in range(1, len(strs)):
            if strs[j][i] != strs[j-1][i]:
                return prefix
                
            
        prefix += strs[0][i]
    
    return prefix
                
