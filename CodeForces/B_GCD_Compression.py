t = int(input())

for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    list_even = []
    list_odd = []
    
    for index, a in enumerate(arr):
        if a % 2 == 0:
            list_even.append(index)
            
        else:
            list_odd.append(index)
            
    num_odd = len(list_odd)
    num_even = 2*n - num_odd
    
    if num_even % 2 == 0:
        #REMOVE TWO EVEN OR TWO ODD
        if num_even == 0:
            list_odd = list_odd[2: ]
        
        else:
            list_even = list_even[2:]
        
                      
    else:
        #REMOVE ONE EVEN AND ONE ODD
        list_even.pop()
        list_odd.pop()
        
    for m in range(0, len(list_even) - 1, 2):
        print(list_even[m] + 1, list_even[m + 1] + 1)

    for m in range(0, len(list_odd) - 1, 2):
        print(list_odd[m] + 1, list_odd[m + 1] + 1)
          
            