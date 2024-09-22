class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        count=Counter(message)
        c=0
        for word in bannedWords:
            if(word in count):
                c+=count[word]
                count.pop(word)
        return c>=2