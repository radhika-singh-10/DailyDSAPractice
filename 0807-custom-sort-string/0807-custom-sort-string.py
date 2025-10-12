class Solution:
    def customSortString(self, order: str, s: str) -> str:
        hm,res=Counter(s),[]
        for ch in order:
            while hm.get(ch,0)>0:
                res.append(ch)
                hm[ch]-=1
            
        for i,c in hm.items():
            res.extend([i]*c)
            
        return ''.join(res)
