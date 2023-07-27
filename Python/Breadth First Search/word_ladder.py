class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        #ADD THE STARTING WORD AND ENDING WORD TO WORDLIST
        wordList.append(beginWord)

        #FIND THE EDGES BETWEEN WORDS
        graph = defaultdict(list)
        def charDiff(word1, word2):
            res = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    res += 1
                    if res > 1:
                        return False

            return res == 1

        for i in range(len(wordList)):
            for j in range(i, len(wordList)):
                word1 = wordList[i]
                word2 = wordList[j]
                if (charDiff(word1, word2)):
                    graph[word1].append(word2)
                    graph[word2].append(word1)
        
        def bfs(begin, target):
            #QUEUE
            q = []
            visited = set()
            q.append((begin, 1))

            while q:
                current, dist = q.pop(0)

                if current == target:
                    return dist

                visited.add(current)
                for i in graph[current]:
                    if i not in visited:
                        q.append((i, dist + 1))

            return 0
        #FIND A PATH BETWEEN BEGINNING TO END
        res = bfs(beginWord, endWord)
        return res
            
