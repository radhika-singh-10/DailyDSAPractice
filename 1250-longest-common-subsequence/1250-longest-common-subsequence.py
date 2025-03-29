class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0
        n,m=len(text1),len(text2)
        dp=[[0]*(m+1) for _ in range(n+1)]
        for i in range(0,n):
            for j in range(0,m):
                if text1[i]==text2[j]:
                    dp[i+1][j+1]=1+dp[i][j]
                else:
                    dp[i+1][j+1]=max(dp[i][j+1],dp[i+1][j])
        return dp[n][m]


                    
