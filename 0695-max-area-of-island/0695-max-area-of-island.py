class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res,R,C,visit=0,len(grid),len(grid[0]),set()
        def dfs(r,c):
            if (r<0 or r>=R or c<0 or c>=C or grid[r][c]==0 or (r,c) in visit):
                return 0

            visit.add((r,c))
            return 1+dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1)

        for i in range(R):
            for j in range(C):
                res=max(res,dfs(i,j))
        return res

