from typing import List

def find_unique_customer_id(customerIDs: List[int]) -> int:
    num = customerIDs[0]
    
    for i in range(1, len(customerIDs)):
        num = num ^ customerIDs[i]
        
    return num
