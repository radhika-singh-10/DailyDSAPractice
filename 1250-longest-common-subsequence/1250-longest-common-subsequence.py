class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n,m,res=len(text1),len(text2),0
        dp=[[0]*(m+1) for _ in range(n+1)]
        for c in reversed(range(m)):
            for r in reversed(range(n)):
                if text2[c]==text1[r]:
                    dp[r][c]=1+dp[r+1][c+1]
                else:
                    dp[r][c]=max(dp[r+1][c],dp[r][c+1])
        return dp[0][0]