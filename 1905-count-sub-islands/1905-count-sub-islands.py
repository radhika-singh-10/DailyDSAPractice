class Solution:
    

        

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def isCellLand(self, x, y, grid):
        return grid[x][y] == 1

    def isSubIsland(self,x,y,grid1,grid2,visited):
        n,m,isSubIsland,pendingCells=len(grid2),len(grid2[0]),True,deque()
        pendingCells.append((x,y))
        visited[x][y]=True
        while pendingCells:
            cur_x,cur_y=pendingCells.popleft()
            if not self.isCellLand(cur_x,cur_y,grid1):
                isSubIsland=False
            for dirs in self.directions:
                next_x,next_y=cur_x+dirs[0],cur_y+dirs[1]
                if (0<=next_x<n and 0<=next_y<m and not visited[next_x][next_y] and self.isCellLand(next_x,next_y,grid2)):
                    pendingCells.append((next_x,next_y))
                    visited[next_x][next_y]=True
        return isSubIsland

    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m,n=len(grid1),len(grid1[0])
        if m==1 and n==1 and grid1[0][0]==1 and grid2[0][0]==1:
            return 1
        elif m==1:
            res,c=0,0
            for i in range(m):
                if grid1[i][0]==1 and grid1[i][0]==grid2[i][0]:
                    c+=1
                    continue
                else:
                    break
            if c>0:
                return 1
            return 0
        elif n==1:
            res=0
            for i in range(m):
                if grid1[0][i]==1 and grid1[0][i]==grid2[0][i]:
                    c+=1
                    continue
                else:
                    break
            if c>0:
                return 1
            return 0
        visited,res=[[False]*n for _ in range(m)],0
        for x in range(m):
            for y in range(n):
                if (not visited[x][y] and self.isCellLand(x,y,grid2) and self.isSubIsland(x,y,grid1,grid2,visited)):
                    res+=1
        return res
        

