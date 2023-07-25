class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        #KEEP TWO POINTERS
        start, end = 0, 1
        max_len, previous_sign = 1, ""
        n = len(arr)

        while end<n:
            if arr[end] > arr[end-1]:
                if previous_sign == "" or previous_sign == "<":
                    max_len = max(max_len, end - start + 1)
                    previous_sign = ">"
                    end+=1

                else:
                    previous_sign = ">"
                    start = end-1
                    end += 1

            elif arr[end] < arr[end-1]:
                if previous_sign == "" or previous_sign == ">":
                    max_len = max(max_len, end - start + 1)
                    previous_sign = "<"
                    end += 1

                else:
                    previous_sign = "<"
                    start = end-1
                    end+=1

            else:
                previous_sign = ""
                start = end
                end += 1
            
        return max_len
                

        return max_len
