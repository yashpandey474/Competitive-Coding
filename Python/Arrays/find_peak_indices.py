def find_peak_indices(sales_data: list[int]) -> list[int]:
    n = len(sales_data)
    result = []
    for i in range(1, len(sales_data)-1):
        
       
        if sales_data[i-1]<sales_data[i] and sales_data[i+1]<sales_data[i]:
            result.append(i)
                
    return result
