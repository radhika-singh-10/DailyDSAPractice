class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        #reinforcement learning concept
        res,n,m=0,len(grid),len(grid[0])
        for i in range(n):
            for j in range(m):
                if i==j==0:
                    continue
                up_path=left_path=float('inf')
                if i!=0:
                    up_path=grid[i][j]+grid[i-1][j]
                if j!=0:
                    left_path=grid[i][j]+grid[i][j-1]
                grid[i][j]=min(up_path,left_path)
        return grid[n-1][m-1]


        #res=grid[n][m]
        # dp=[[0]*m for _ in range(n)]
        # for i in range(n-1,-1,-1):
        #     for j in range(m-1,-1,-1):
        #         if i==n-1 and j!=m-1:
        #             dp[i][j]=grid[i][j]+dp[i][j+1]
        #         elif i!=n-1 and j==m-1:
        #             dp[i][j]=grid[i][j]+dp[i+1][j]
        #         elif i!=n-1 and j!=m-1:
        #             dp[i][j]=grid[i][j]+min(dp[i+1][j],dp[i][j+1])
        #         else:
        #             dp[i][j] = grid[i][j]
        #         # res+=min(grid[i-1][j],grid[i][j-1])
        #         # print(res,grid[i-1][j],grid[i][j-1])

        # return dp[0][0]