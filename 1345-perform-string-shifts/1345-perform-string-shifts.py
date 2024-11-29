class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        x=0
        for d,a in shift:
            if d==0:
                x-=a
            else:
                x+=a
        res=[None]*len(s)
        for i,ch in enumerate(s):
            res[(i+x)%len(s)]=ch
        return "".join(res)

            
