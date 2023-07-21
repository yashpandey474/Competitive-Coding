def top_k_frequent_products(products: list[int], k: int) -> list[int]:
    #MAP TO STORE ELEMENTS  WITH FREQUENCIES
    map_freq = {}
    for i in products:
        if i in map_freq:
            map_freq[i] += 1
        else:
            map_freq[i] = 0
            
    #CREATE MAX-HEAP
    heap = []
    for product, freq in sorted(map_freq.items()):
        if len(heap)<k:
            heap.append(product)
        else:
            break
        
    return heap
