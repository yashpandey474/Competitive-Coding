# Union just
from typing import Union

def reverse_in_place(s: Union[str, int]) -> Union[str, int]:
    if isinstance(s, str):
        ans = ""
        j = len(s)-1
        while(j>=0):
            ans += s[j]
            j-=1
        return ans
        
    elif(isinstance(s, int)):
        #REVERSE INTEGER
        ans = 0
        while(s>0):
            ans = (ans*10) + s%10
            s = int(s/10)
            
        return ans
    
    else:
        raise TypeError()
    return s
