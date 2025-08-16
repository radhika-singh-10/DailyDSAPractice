from collections import deque
class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        m, n = len(grid), len(grid[0])
        dirs = [(-1, 0, 'U'), (0, -1, 'L'), (1, 0, 'D'), (0, 1, 'R')]
        shapes = set()

        def bfs(i, j):
            queue = deque()
            queue.append((i, j))
            grid[i][j] = -1
            path = ['S']  

            while queue:
                r, c = queue.popleft()
                for dx, dy, dir_char in dirs:
                    nr, nc = r + dx, c + dy
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                        grid[nr][nc] = -1
                        queue.append((nr, nc))
                        path.append(dir_char)
                        #print(nr,nc)
                    path.append('E')  
            #print(i, j,''.join(path))
            return ''.join(path)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    shape = bfs(i, j)
                    shapes.add(shape)

        return len(shapes)










