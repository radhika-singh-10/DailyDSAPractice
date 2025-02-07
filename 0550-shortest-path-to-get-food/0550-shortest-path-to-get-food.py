class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        dirs=[[-1,0],[0,-1],[1,0],[0,1]]
        n,m=len(grid),len(grid[0])
        food_pos=set()
        initial_row, initial_col = -1, -1
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '*':
                    initial_row, initial_col = i, j
                    break
            if initial_row != -1:
                break
 
        res=0
        queue=deque([(initial_row, initial_col ,0)])
        visited=set((initial_row, initial_col))
        while queue:
            r, c, steps = queue.popleft()

            if grid[r][c] == '#':
                return steps

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m and (nr, nc) not in visited and grid[nr][nc] != 'X':
                    visited.add((nr, nc))
                    queue.append((nr, nc, steps + 1))
        return -1
          



        # def dfs(grid,r,c):
        #     if min(r,c)<0 or r==n or c==m or (r,c) in visit or grid[r][c]=='X':
        #         return 0
        #     if grid[r][c]=='#':
        #         return 1
        #     visit.add((r,c))
        #     count=0
        #     count=1+min(count,dfs(grid,r-1,c), dfs(grid,r+1,c), dfs(grid,r,c-1), dfs(grid,r,c+1))
        #     visit.remove((r,c))
        #     return count

        # res=min(res, dfs(grid,initial_row, initial_col))

        # return res if res>0 else -1
