class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        #dfs
        #n2 - tc, sc
        dirs=[[-1,0],[0,-1],[1,0],[0,1]]
        n,m=len(mat),len(mat[0])
        res=res = [[float('inf')] * m for _ in range(n)]
        queue = deque()
        
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    res[i][j] = 0
                    queue.append((i, j))
        
        while queue:
            r,c=queue.popleft()
            for dr,dc in dirs:
                nr,nc=r+dr,c+dc
                if 0<=nr<n and 0<=nc<m and res[nr][nc]>res[r][c]:
                    res[nr][nc]=res[r][c]+1
                    queue.append((nr,nc))
            
        return res