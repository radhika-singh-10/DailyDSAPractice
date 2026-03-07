class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res=""
        p1,p2,n=0,0,max(len(word1),len(word2))
        for i in range(n):
            if i<len(word1):
                res+=word1[i]
            if i<len(word2):
                res+=word2[i]
        return "".join(res)