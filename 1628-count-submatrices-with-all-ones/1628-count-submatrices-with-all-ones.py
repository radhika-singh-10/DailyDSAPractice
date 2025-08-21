class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m,n=len(mat),len(mat[0])
        dp,res=[[0]*n for _ in range(m)],0
        for i in range(m):
            for j in range(n):
                if j==0:
                    dp[i][j]=mat[i][j]
                else:
                    dp[i][j]=0 if mat[i][j]==0 else 1+dp[i][j-1]
                cur=dp[i][j]
                for k in range(i,-1,-1):
                    cur=min(cur,dp[k][j])
                    if cur==0:
                        break
                    res+=cur
        return res  
                   
            