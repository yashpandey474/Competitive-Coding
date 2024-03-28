

def find_smallest_string(s):
    n = len(s)
    for i in range(1, n+1):
        if n % i == 0:
            substring = s[:i]
            repeated_string = substring * (n // i)
            if repeated_string == s:
                return substring
    return None

# Example usage
s = "abcabcab"
smallest_string = find_smallest_string(s)
print(smallest_string)