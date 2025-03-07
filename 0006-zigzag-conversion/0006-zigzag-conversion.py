from collections import defaultdict
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s)==1 or numRows == 1 or numRows >= len(s):
            return s
        res=[[] for _ in range(numRows)]
        i,d=0,1
        for ch in s:
            res[i].append(ch)
            if i==0:
                d=1
            elif i==numRows-1:
                d=-1
            i+=d
        for i in range(numRows):
            res[i]=''.join(res[i])
        return "".join(res)
        
