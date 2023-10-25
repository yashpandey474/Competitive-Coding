
def detect_duplicate_products(product_ids: list[int]) -> bool:
    #SORT THE ARRAY
    product_ids = sorted(product_ids)
    
    #FIND ANY DUPLICATES
    for i in range(1, len(product_ids)):
        if(product_ids[i] == product_ids[i-1]):
            return True
            
    return False
#OR: return len(product_ids) != len(set(product_ids))
