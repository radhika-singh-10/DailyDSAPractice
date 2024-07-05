class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        res,count=0,0
        for i in range(len(grid)):
            for j in range(len(grid)):
                res+=1
                for k in range(len(grid)):
                    if grid[i][k]!=grid[k][j]:
                        res-=1
                        break  
        return res