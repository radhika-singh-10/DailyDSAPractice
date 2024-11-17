class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
        n, m, res = len(mat), len(mat[0]), []
        
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