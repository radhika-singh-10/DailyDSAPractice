from collections import defaultdict
class Solution:
    def findValidPair(self, s: str) -> str:
        occurence,res,n=Counter(s),"",len(s)
        for i in range(n-1):
            a,b=s[i],s[i+1]
            if a!=b and occurence[a]==int(a) and occurence[b]==int(b):
                return a+b

        return ""