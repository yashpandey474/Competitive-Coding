def search(arr, target) :
    # Write your code here.
    
    #BINARY SEARCH
    low = 0
    high = len(arr)-1

    while low<=high:
        mid = (low+high)//2

        if arr[mid] == target:
            return mid

        #  current left half is sorted
        if arr[low] <= arr[mid]:
            #search in left
            if target < arr[mid] and target >= arr[low]:
                high = mid-1

            else:
                low = mid+1

        
        # current right half is sortd
        else:
            # search in right
            if target > arr[mid] and target <= arr[high]:
                low = mid+1

            else:
                high = mid-1

        


    return -1
