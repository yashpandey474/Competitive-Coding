
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:


        #IMPLEMENTATION WITHOUT TRIE

        #SORT THE ARRAY 
        products = sorted(products)
        left = 0
        right = len(products)-1
        result = []

        #ITERATE FOR EVERY CHARACTER IN SEARCH WORD
        for j in range(len(searchWord)):
            #MOVE LEFT FORWARD UNTIL MATCHING PREFIX
            while left <= right and (len(products[left]) <= j or products[left][j] != searchWord[j]):
                left += 1
            #MOVE RIGHT BACK UNTIL MATCHING PREFIX
            while right >= left and (len(products[right]) <= j or products[right][j] != searchWord[j]):
                right-=1

            #IF ALL CHECKED
            if left > right:
                print("EMPTY ADDED J = ", j)
                for m in range((len(searchWord)-j)):
                    result.append([])
                break

            
            #ADD FIRST THREE
            result.append(products[left: min(left + 3, right + 1)])
            
        
        return result
            
