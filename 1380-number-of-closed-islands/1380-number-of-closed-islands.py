class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        n,m=len(grid),len(grid[0])
        
        res,visited=0,set()
        dirs=[[0,1],[1,0],[0,-1],[-1,0]]
        
        def bfs(r,c):
            queue = collections.deque()
            queue.append((r, c))
            visited.add((r, c))
            is_closed = True 
            while queue:
                r, c = queue.popleft()
                if r == 0 or c == 0 or r == n - 1 or c == m - 1:
                    is_closed = False  
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 0 and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        queue.append((nr, nc))

            return is_closed

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0 and (i, j) not in visited:
                    if bfs(i, j):
                        res += 1

        return res
                    
