from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res,m,n = 0,len(grid),len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    grid[i][j] = '0'
                    self.bfs(grid,i,j)
                    res += 1
        return res

    def bfs(self,grid,i,j):
        queue = deque([(i,j)])
        while queue:
            I,J = queue.popleft()
            for i,j in [I+1,J],[I,J+1],[I-1,J],[I,J-1]:
                if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == '1':
                    grid[i][j] = '0'
                    queue.append((i,j))