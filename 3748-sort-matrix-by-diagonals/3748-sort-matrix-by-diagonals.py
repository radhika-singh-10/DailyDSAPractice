
class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        hm,n=defaultdict(list),len(grid)
        for i in range(n):
            for j in range(n):
                if i-j>=0:
                    heappush(hm[i-j],-grid[i][j])
                    #print(hm[i-j])
                else:
                    heappush(hm[i-j],grid[i][j])
            

        for i in range(n):
            for j in range(n):
                if i-j>=0:
                    #print(hm[i-j])
                    grid[i][j]=-heappop(hm[i-j])
                    #print(grid[i][j])
                else:
                    grid[i][j]=heappop(hm[i-j])
        return grid
                

