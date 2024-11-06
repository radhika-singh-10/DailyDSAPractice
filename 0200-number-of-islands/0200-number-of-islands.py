from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        res,visited,queue,rows,cols=0,set(),deque(),len(grid),len(grid[0])
        #bfs
        def bfs():
            while queue:
                row,col=queue.popleft()
                dirs=[[1,0],[-1,0],[0,1],[0,-1]]
                for dr,dc in dirs:
                    r,c=row+dr,col+dc
                    if (r in range(rows) and c in range(cols) and grid[r][c]=='1' and (r,c) not in visited):
                        queue.append((r,c))
                        visited.add((r,c))


        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=="1" and (i,j) not in visited:
                    queue.append((i,j))
                    visited.add((i,j))
                    res+=1
                    bfs()
        return res