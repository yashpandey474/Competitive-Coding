from typing import List

def find_increasing_trend(prices: List[int]) -> bool:
    #FIND A TRIPLET OF INCREASING PRICES
    first = float('inf')
    second = float('inf')
    n = len(prices)
    for i in range(n):
        if prices[i] <= first:
            first = prices[i]
            
        elif prices[i] <= second:
            second = prices[i]
            
        else:
            return True
        
    return False
                
    
