class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        return [idx for idx,word in enumerate(words) if word.find(x)!=-1]
        