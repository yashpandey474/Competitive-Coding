def recursion(products, result, current_index, answer):
    if current_index >= len(products):
        if answer not in result:
            result.append(answer)
        return
    #0-1 KNAPSACK
    recursion(products, result, current_index+1, answer + [products[current_index]])
    recursion(products, result, current_index+1, answer)
    
def generate_subsets(products: list[int]) -> list[list[int]]:
    #0-1 KNAPSACK PROBLEM OR GENERATING SUBSEQUENCE
    result = []
    recursion(products, result, 0, [])
    return sorted(result)
