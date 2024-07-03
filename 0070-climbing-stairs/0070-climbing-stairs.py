class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        else:
            dp=[0]*(n+1)
            dp[0],dp[1],dp[2]=0,1,2
            i=3
            res=0
            while i<=n:
                dp[i]=dp[i-1]+dp[i-2]
                i=i+1
            return dp[n]