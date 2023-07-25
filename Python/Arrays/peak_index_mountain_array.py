class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        start = 0
        end = n-1

        while start <= end:
            mid = (start + end)//2

            if mid == 0:
                if arr[mid] > arr[mid + 1]:
                    return mid
                start = mid + 1
                continue

            if mid == n-1:
                if arr[mid] > arr[mid-1]:
                    return mid
                end = mid - 1
                continue

            if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid+1]:
                return mid

            if arr[mid] < arr[mid-1]:
                end = mid - 1

            if arr[mid] < arr[mid+1]:
                start = mid + 1

        return start
