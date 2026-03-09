class Solution:
    def longestBalanced(self, s: str) -> int:
        res,n=0,len(s)
        for i in range(n):
            occurence=defaultdict(int)
            for j in range(i,n):
                occurence[s[j]]+=1
                if len(set(occurence.values()))==1:
                    res=max(res,j-i+1)
        return res



