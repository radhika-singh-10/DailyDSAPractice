class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        n,m,area=len(grid),len(grid[0]),float('inf')
        #find the 1s positions - perform a search - bfs/dfs
        min_i,min_j,max_i,max_j=n,m,0,0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    #perform bfs
                    min_i=min(min_i,i)
                    min_j=min(min_j,j)
                    max_i=max(max_i,i)
                    max_j=max(max_j,j)
        return (max_j-min_j+1)*(max_i-min_i+1)

