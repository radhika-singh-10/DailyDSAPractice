class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n,m,fresh=len(grid),len(grid[0]),0
        queue=deque()
        minutes=0
        directions=[[1,0],[0,1],[-1,0],[0,-1]]
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    fresh+=1
                elif grid[i][j]==2:
                    queue.append((i,j))
        
        
        while queue and fresh>0:
            for i in range(len(queue)):
                r,c=queue.popleft()
                for dr,dc in directions:
                    if 0<=r+dr<n and 0<=c+dc<m and grid[r+dr][c+dc]==1:
                        grid[r+dr][c+dc]=2
                        queue.append((r+dr,c+dc))
                        fresh-=1
            minutes+=1

        return minutes if fresh ==0 else -1      