class Trie:
    def __init__(self):
        self.children = [None]*26
        self.word = None

class Solution:
   
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        #GET DIMENSIONS
        rows, columns = len(board), len(board[0])

        self.root = Trie()
        result = set()

        def insertWord(string):
            current = self.root

            for i in string:
                letter = ord(i) - ord('a')
                if current.children[letter] is None:
                    current.children[letter] = Trie()
                current = current.children[letter]

            current.word = string

        def dfs(row, column, root, visited):
            #CHECK OUT OF BOUNDS OR ALREADY VISITED
            if row < 0 or row >= rows or column < 0 or column >= columns or (row, column) in visited:
                return

            #CHECK IF ROOT IS NONE OR DON'T MATCH
            letter = ord(board[row][column]) - ord('a')
            if not root or not root.children[letter]:
                return
            
            #CHECK IF IS WORD
            root = root.children[letter]
            if root.word:
                result.add(root.word)

            #ADD TO VISITED
            visited.add((row, column))

            #PASS TO ALL OTHERS
            dfs(row + 1, column, root, visited)
            dfs(row - 1, column, root, visited)
            dfs(row, column + 1, root, visited)
            dfs(row, column - 1, root, visited)

            visited.remove((row, column))

        
        #INSERT THE WORDS INTO A TRIE
        for i in words:
            insertWord(i)

        #SEARCH FOR WORDS ON BOARD
        for i in range(rows):
            for j in range(columns):
                #CHECK IF EXISTS AS FIRST LETTER
                letter = board[i][j]
                letter_num = ord(letter) - ord('a')
                #IF IT IS FIRST LETTER OF SOME WORD
                if self.root.children[letter_num] is not None:
                    #RUN DFS: SHOULD DETECT IF HAS A WORD POSSIBLE AND ADD TO RESULT
                    dfs(i, j, self.root, set())

        return list(result)
                
        

        
