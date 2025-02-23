# from collections import deque
class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        res = 0
        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        m, n = len(grid), len(grid[0])
        visited = set() 
        
        def bfs(r, c):
            queue = deque()
            queue.append((r, c))
            visited.add((r, c))
            fish_count = 0
            
            while queue:
                x, y = queue.popleft()
                fish_count += grid[x][y]
                for dx, dy in dirs:
                    rx, ry = x + dx, y + dy  
                    if 0 <= rx < m and 0 <= ry < n and grid[rx][ry] > 0 and (rx, ry) not in visited:
                        queue.append((rx, ry))
                        visited.add((rx, ry))
            return fish_count
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0 and (i, j) not in visited:
                    res = max(res, bfs(i, j))
                    
        return res