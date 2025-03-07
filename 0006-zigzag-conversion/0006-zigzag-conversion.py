from collections import defaultdict
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s)==1 or numRows == 1 or numRows >= len(s):
            return s
        res=[[] for _ in range(numRows)]
        i,counter=0,1
        for ch in s:
            res[i].append(ch)
            #print(i,counter,ch)
            if i==0:
                counter=1
            elif i==numRows-1:
                counter=-1
            i+=counter
        for i in range(numRows):
            res[i]=''.join(res[i])
        return "".join(res)
        
