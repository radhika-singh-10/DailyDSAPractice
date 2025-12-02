class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        res,cur=0,float('-inf')
        pairs.sort(key=lambda x: (x[1],x[0]))
        for pair in pairs:
            if pair[0]>cur:
                res+=1
                cur=pair[1]
        return res

