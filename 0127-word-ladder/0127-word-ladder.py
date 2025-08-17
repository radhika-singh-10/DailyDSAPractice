class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if (endWord not in wordList or not beginWord or not endWord or not wordList): 
            return 0

        wordSet = set(wordList)
        beginSet = {beginWord}
        endSet = {endWord}
        visited = set()
        res = 1
        
        while beginSet and endSet:
            if len(beginSet) > len(endSet):
                beginSet, endSet = endSet, beginSet
            
            next_set = set()
            
            for word in beginSet:
                for i in range(len(word)):
                    for c in string.ascii_lowercase:
                        if c == word[i]:
                            continue
                        
                        new_word = word[:i] + c + word[i+1:]
                        
                        if new_word in endSet:
                            return res + 1
                        
                        if new_word in wordSet and new_word not in visited:
                            visited.add(new_word)
                            next_set.add(new_word)
            
            beginSet = next_set
            res += 1
        
        return 0
