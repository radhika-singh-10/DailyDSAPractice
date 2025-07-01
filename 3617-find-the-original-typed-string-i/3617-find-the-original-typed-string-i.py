from collections import defaultdict
class Solution:
    def possibleStringCount(self, words: str) -> int:
        n,res=len(words),1
        for i in range(1,n):
            if words[i]==words[i-1]:
                res+=1
        return res