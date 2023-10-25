def increment_large_integer(digits: list[int]) -> list[int]:
    rem = 1
    
    for i in range(len(digits)-1, -1, -1):
        current = digits[i] + rem
        digits[i] = current%10
        rem = int(current/10)
        print("DIGIT = ", digits[i], " SUM = ", current, " REM = ", rem)

    
    if(rem == 1):
        digits.insert(0, 1)
        
    return digits
        
