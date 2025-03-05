class Solution:
    def reverseWords(self, s: str) -> str:
        #split string words - list
        #reverse it and join it

        words=s.split()
        words=words[::-1]
        return ' '.join(words)
