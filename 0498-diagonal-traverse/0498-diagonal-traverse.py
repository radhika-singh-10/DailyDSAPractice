class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
        n, m, res = len(mat), len(mat[0]), []

        # brute force
        # valueStorage=collections.defaultdict(list)
        # for i in range(n):
        #     for j in range(m):
        #         valueStorage[(i+j)].append(mat[i][j])
        # for key,val in valueStorage.items():
            
        #     if key%2!=0:
        #         for v in range(len(val)):
        #             res.append(val[v])
        #     else:
        #         for v in range(len(val)-1,-1,-1):
        #             res.append(val[v])
        # return res
        
        for d in range(n + m - 1):  
            if d % 2 == 0:  
                r = min(d, n - 1)
                c = d - r
                while r >= 0 and c < m:
                    res.append(mat[r][c])
                    r -= 1
                    c += 1
            else:  
                c = min(d, m - 1)
                r = d - c
                while r < n and c >= 0:
                    res.append(mat[r][c])
                    r += 1
                    c -= 1
        
        return res