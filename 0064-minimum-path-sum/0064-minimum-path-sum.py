class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for j in range(1, n):
            grid[0][j] += grid[0][j - 1]
        for i in range(1, m):
            grid[i][0] += grid[i - 1][0]
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])

        return grid[m - 1][n - 1]
        # #reinforcement learning concept
        # res,n,m=0,len(grid),len(grid[0])
        # for i in range(n):
        #     for j in range(m):
        #         if i==j==0:
        #             continue
        #         up_path=left_path=float('inf')
        #         if j!=0:
        #             left_path=grid[i][j-1]+grid[i][j]
        #         if i!=0:
        #             up_path=grid[i-1][j]+grid[i][j]
        #         grid[i][j]=min(up_path,left_path)
        # return grid[-1][-1]
                




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