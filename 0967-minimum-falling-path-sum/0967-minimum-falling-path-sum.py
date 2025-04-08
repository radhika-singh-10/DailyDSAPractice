class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n,res=len(matrix),float("inf")
        dp=[[0]*(n+1) for _ in range(n+1)]
        for i in range(n-1,-1,-1):
            for j in range(0,n):
                if j==0:
                    dp[i][j]=min(dp[i+1][j],dp[i+1][j+1])+matrix[i][j]
                elif j==n-1:
                    dp[i][j]=min(dp[i+1][j],dp[i+1][j-1])+matrix[i][j]
                else:
                    dp[i][j]=min(dp[i+1][j],dp[i+1][j-1],dp[i+1][j+1])+matrix[i][j]
        for i in range(n):
            res=min(res,dp[0][i])
        
        return res
        
        # r,c,min_val=0,0,matrix[0][0]
        # for i in range(1,m):
        #     if min_val>matrix[0][i]:
        #         min_val=matrix[0][i]
        #         c=i

        # for i in range(r+1,n):
        #     if c==0:
        #         if matrix[i][c+1]<=matrix[i][c]:
        #             min_val+=matrix[i][c+1]
        #             c=c+1
        #         else:
        #             min_val+=matrix[i][c]
        #     elif c==m-1:
        #         if matrix[i][c-1]<=matrix[i][c]:
        #             min_val+=matrix[i][c-1]
        #             c=c-1
        #         else:
        #             min_val+=matrix[i][c]
        #     else:
        #         if matrix[i][c-1]<=matrix[i][c] and matrix[i][c]<=matrix[i][c+1]:
        #             min_val+=matrix[i][c-1]
        #             c=c-1
        #         elif matrix[i][c+1]<=matrix[i][c-1] and (matrix[i][c-1]<=matrix[i][c+1] or matrix[i][c]<matrix[i][c-1]):
        #             min_val+=matrix[i][c]
        #             c=c+1
        #         else:


        #         min_val+=min(matrix[i][c-1],matrix[i][c],matrix[i][c+1])
        # return min_val
            




                





