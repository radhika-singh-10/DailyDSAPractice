class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        n,m=len(word1),len(word2)
        if n==0:
            return m
        if m==0:
            return n
        dp=[[0] * (m + 1) for _ in range(n + 1)]
        for i in range(1,n+1):
            dp[i][0]=i
        for j in range(1,m+1):
            dp[0][j]=j
        for i in range(1,n+1):
            for j in range(1,m+1):
                if word2[j-1]==word1[i-1]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j]=min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
        return dp[n][m]

        # def minDistanceRecursion(word1,word2,n,m,dp):
        #     if n==0:
        #         return m
        #     elif m==0:
        #         return n
        #     elif dp[n][m] is not None:
        #         return dp[n][m]
        #     if word1[n-1]==word2[m-1]:
        #         dp[n][m]  = minDistanceRecursion(word1,word2,n-1,m-1,dp)
        #     else:
        #         dp[n][m] = 1+min(
        #             minDistanceRecursion(word1,word2,n-1,m-1,dp), #replace
        #             minDistanceRecursion(word1,word2,n-1,m,dp), #delete or remove
        #             minDistanceRecursion(word1,word2,n,m-1,dp)) #insert
        #     return dp[n][m] 

        # n,m=len(word1),len(word2)
        # dp=[[None] * (m + 1) for _ in range(n + 1)]
        # return minDistanceRecursion(word1,word2,n,m,dp)


        
        
