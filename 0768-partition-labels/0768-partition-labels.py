class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        occurence=[0]*26
        for i,ch in enumerate(s):
            occurence[ord(ch)-ord("a")]=i
        start,end=0,0
        res=[]
        for idx, ch in enumerate(s):
            end=max(end,occurence[ord(ch)-ord("a")])
            if idx==end:
                res.append(idx-start+1)
                start=idx+1
        return res

        