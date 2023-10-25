def product_of_prices(prices: list[int]) -> list[int]:
    n = len(prices)
    left, right, result = [0]*n, [0]*n, [0]*n
    
    left[0], right[n-1] = 1, 1

    for i in range(1, n):
        left[i] = left[i-1]*prices[i-1]
        
    for i in range(n-2,-1, -1):
        right[i] = right[i+1]*prices[i+1]
        
    for i in range(n):
        result[i] = left[i]*right[i]
    
    return result
    
