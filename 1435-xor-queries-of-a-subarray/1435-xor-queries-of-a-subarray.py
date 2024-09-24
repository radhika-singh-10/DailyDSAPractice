class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n,m=len(queries),len(arr)
        res,prefix=[]*n,[0]*(m+1)
        for i in range(m):
            prefix[i+1]=prefix[i]^arr[i]
        for i in range(n):
            l,r=queries[i][0],queries[i][1]
            res.append(prefix[r+1]^prefix[l])
        return res