t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    
    freq = {}
    
    for i in s:
        if i not in freq:
            freq[i] = 0
            
        freq[i] += 1
        
    i = 0
    all_set = set()
    max_val = 0
    
    while i < n:
        all_set.add(s[i])
        freq[s[i]] -= 1
        
        if freq[s[i]] == 0:
            del freq[s[i]]
            
        max_val = max(
            max_val,
            len(all_set) + len(freq)
        )
        i += 1
    print(max_val)