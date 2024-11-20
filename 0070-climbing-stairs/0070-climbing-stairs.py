class Solution:
    def climbStairs(self, n: int) -> int:
        #base case, recurrence formula ,recurrence 
        if n<=2:
            return n
        elif n<=0:
            return 0
        else:
            dp=[0]*(n+1)
            dp[0],dp[1]=1,1
            res=0
            for i in range(2,n+1): 
                dp[i]=dp[i-1]+dp[i-2]
            return dp[n]

            #time limit exceeded
            # def recursion(n):
            #     if n<=0:
            #         return 0
            #     elif 1<=n<=2:
            #         return n
            #     else:

            #         return recursion(n-1)+recursion(n-2)

            # return recursion(n)