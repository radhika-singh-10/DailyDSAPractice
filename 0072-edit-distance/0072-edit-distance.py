class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def minDistanceRecursion(word1,word2,n,m,dp):
            if n==0:
                return m
            elif m==0:
                return n
            elif dp[n][m] is not None:
                return dp[n][m]
            if word1[n-1]==word2[m-1]:
                dp[n][m]  = minDistanceRecursion(word1,word2,n-1,m-1,dp)
            else:
                dp[n][m] = 1+min(
                    minDistanceRecursion(word1,word2,n-1,m-1,dp), #replace
                    minDistanceRecursion(word1,word2,n-1,m,dp), #delete or remove
                    minDistanceRecursion(word1,word2,n,m-1,dp)) #insert
            return dp[n][m] 

        n,m=len(word1),len(word2)
        dp=[[None] * (m + 1) for _ in range(n + 1)]
        return minDistanceRecursion(word1,word2,n,m,dp)


        
        
