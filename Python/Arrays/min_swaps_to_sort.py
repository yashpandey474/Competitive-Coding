def minSwaps(arr):
    # Write your code here.
    
    #SORTED ARRAY
    temp = sorted(arr)
    result = 0
    #CREATE A MAP FOR INDICES
    map_index = {num: i for i, num in enumerate(arr)}


    #ITERATE
    for i in range(len(arr)):
        #CHECK IF EQUAL
        if temp[i] != arr[i]:
            result += 1
            #EXCHANGE
            index = map_index[temp[i]]
            arr[i], arr[index] = arr[index], arr[i]

            map_index[arr[index]] = index

    return result

