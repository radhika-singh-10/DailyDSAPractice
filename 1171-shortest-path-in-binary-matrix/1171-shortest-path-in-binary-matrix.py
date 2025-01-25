from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n,m,visited,queue=len(grid),len(grid[0]),set(),deque()
        dirs=[(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,-1),(-1,1),(1,-1)]
        if grid[0][0]==1 or grid[n-1][m-1]==1:
            return -1
        visited.add((0,0))
        queue.append((1,0,0))
        while queue:
            d,r,c=queue.popleft()
            if r == n-1 and c == m-1:
                return d
            for x,y in dirs:
                rx,ry = r+x,c+y
                if 0<=rx<n and 0<=ry<m and grid[rx][ry]==0 and (rx,ry) not in visited:
                    visited.add((rx,ry))
                    queue.append((d+1,rx,ry))

        return -1
            
