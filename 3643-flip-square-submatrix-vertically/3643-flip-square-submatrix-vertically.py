class Solution:
    def reverseSubmatrix(self, grid, x,y,z):
        m,n=len(grid),len(grid[0])
        for i in range(z//2):
            for j in range(z):
                grid[x+i][y+j],grid[x+z-1-i][y+j]=grid[x+z-1-i][y+j],grid[x+i][y+j]
        return grid
