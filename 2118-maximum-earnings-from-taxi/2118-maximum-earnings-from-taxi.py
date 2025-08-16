class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        #sort by start times
        #apply dp - get optimal
        rides.sort(key=lambda x:x[0])
        dp=[0]*(n+1)
        for i in range(n-1,-1,-1):
            dp[i]=dp[i+1]
            while rides and i==rides[-1][0]:
                s,e,t=rides.pop()
                dp[i]=max(dp[i],dp[e]+e-s+t)
        return dp[0]