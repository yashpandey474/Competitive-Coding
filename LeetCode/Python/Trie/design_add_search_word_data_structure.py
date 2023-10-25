class Trie:
    def __init__(self):
        self.children = [None]*26
        self.isWord = False
class WordDictionary:

    def __init__(self):
        self.root = Trie()
        

    def addWord(self, string: str) -> None:
        current = self.root
        for i in string:
            letter = ord(i) - ord('a')
            if current.children[letter] is None:
                current.children[letter] = Trie()

            current = current.children[letter]

        current.isWord = True
        
    def searchWord(self, string, root):
        current = root
        for i in range(len(string)):
            char = string[i]
            if char == ".":
                for t in current.children:
                    if t and self.searchWord(string[i+1:], t):
                        return True
                return False
                        
            letter = ord(char) - ord('a')
            if current.children[letter] is None:
                return False
            current = current.children[letter]

        return current.isWord

    def search(self, string: str) -> bool:
        return self.searchWord(string, self.root)
        
            


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
