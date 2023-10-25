
def recGen(chars: list[str], answer:list[int], result, used):
    if(len(answer) == len(chars)):
        result.append(answer)
        return
    
    for i in range(len(chars)):
        if i not in used or used[i] == False:
            used[i] = True
            recGen(chars, answer + chars[i], result, used)
            used[i] = False
    
    
        
def generate_product_names(chars: list[str]) -> list[str]:
    result = []
    used = {}
    
    if not chars:
        return result
    recGen(chars, "", result, used)
    return result
