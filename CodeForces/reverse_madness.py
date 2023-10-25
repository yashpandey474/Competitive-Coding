t = int(input())

for testcase in range(t):
    n, k = map(int, input().split())
    string = list(input())
    l = list(map(int, input().split()))
    r = list(map(int, input().split()))
    q = int(input())
    x = list(map(int, input().split()))
    
    for ele in x:
        st = 0
        en = k - 1
        
        while st < en:
            mid = st + (en - st)//2
            
            if l[mid] <= ele <= r[mid]:
                a = min(ele, r[mid] + l[mid] - ele)
                b = max(ele, r[mid] + l[mid] - ele)
                
                a -= 1
                b -= 1
                string[a:b+1] = string[a:b+1][::-1]
                break
            elif ele < l[mid]:
                en = mid - 1
                
            elif ele > r[mid]:
                st = mid + 1
                
    print("".join(string))                