class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        hm={}
        for i,j in items:
            if i in hm:
                hm[i].append(j)
            else:
                hm[i]=[j]

        res=sorted([[k,sum(sorted(v,reverse=True)[:5])//5] for k,v in hm.items()])
        return res

