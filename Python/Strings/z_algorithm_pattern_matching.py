from typing import List

def search(s: str, pattern: str) -> List[int]:
    # Write your code here.
    


    #CREATE THE Z-STRING
    z_string = pattern + "$" + s
    #CREATE THE Z-ARRAY
    len_pat = len(pattern)
    len_z = len(z_string)
    z_array = [0]*len_z

    #ITERATE THROUGH THE Z-STRING: STARTING FROM TEXT
    for i in range(len_pat+1, len_z):
        #CHECK IF IT MATCHES FIRST LETTER OF STRING
        if z_string[i] == z_string[0]:
            result = 1
            p = 1
            store_i = i
            i = i+1
            while p<len_pat and i<len_z and z_string[i] == z_string[p]:
                result += 1
                i+=1
                p+=1
            
            z_array[store_i] = result
            i = store_i
    #ITERATE THROUGH ARRAY
    result = []
    for i in range(len_z):
        if z_array[i] == len_pat:
            result.append(i-len_pat)

    return result
