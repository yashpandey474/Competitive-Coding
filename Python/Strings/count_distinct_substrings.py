def countDistinctSubstrings(s):
    # Write your code here
    res = set()
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            res.add(s[i:j])

    return len(res)+1
