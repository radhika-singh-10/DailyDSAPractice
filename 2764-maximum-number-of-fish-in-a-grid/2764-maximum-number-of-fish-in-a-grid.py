from collections import deque
class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        res=0
        dirs=[[1,0],[0,1],[-1,0],[0,-1]]
        m,n=len(grid),len(grid[0])
        land,queue=[[False]*n for _ in range(m)],deque()
        def dfs(r,c):
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 0 or land[r][c]:
                return 0
            land[r][c]=True
            return (grid[r][c] +
                    dfs(r - 1, c) +
                    dfs(r + 1, c) +
                    dfs(r, c - 1) +
                    dfs(r, c + 1))


        for i in range(m):
            for j in range(n):
                if grid[i][j]>0 and not land[i][j]:
                    #apply dfs and compare the maximum fish collected from that location to the next location where grid[r][c]>0
                    
                    res=max(res,dfs(i,j))

        return res
                    

            