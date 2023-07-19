

def merge(arr1, start1, end1, arr2, start2, end2):
    i = start1
    j = start2
    arr3 = []

    while i<=end1 and j<=end2:
        if arr1[i] <= arr2[j]:
            arr3.append(arr1[i])
            i+=1

        else:
            arr3.append(arr2[j])
            j+=1

    arr3.extend(arr1[i:end1+1])
    arr3.extend(arr2[j:end2+1])
    arr1[start1:end2+1] = arr3[:]
    
def mergeSort(arr: [int], l: int, r: int):
    # Write Your Code Here
    if l<r:
        mid = (l+r)//2
        mergeSort(arr, l, mid)
        mergeSort(arr, mid+1, r)
        merge(arr, l, mid, arr, mid+1, r)


