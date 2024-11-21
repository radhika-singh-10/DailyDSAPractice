class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res,comb=[],[]
        
        def combination(i):
            if len(comb)==k:
                res.append(comb[:])
                return 

            for j in range(i,n+1):
                comb.append(j)
                combination(j+1)
                comb.pop()

        combination(1)
        return res