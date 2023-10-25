from typing import List
def max_profit(prices: List[float]) -> float:
    if(len(prices) <= 1):
        return 0
        
    min_val = prices[0]
    profit = 0
        
    for i in range(1, len(prices)):
        if(prices[i] < min_val):
            min_val = prices[i]
        
        else:
            profit = max(profit, prices[i] - min_val)
            
    return profit
