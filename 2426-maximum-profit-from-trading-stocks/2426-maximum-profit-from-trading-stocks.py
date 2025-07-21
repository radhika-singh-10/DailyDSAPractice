class Solution:
    def maximumProfit(self, present: List[int], future: List[int], budget: int) -> int:
        n=len(present)
        dp = [0 for _ in range(budget + 1)]
        for f,p in zip(future,present):
            #print(p-1)
            for i in range(budget,p-1,-1):
                
                dp[i]=max(dp[i],f-p+dp[i-p])
            #print(dp)
        return dp[budget]
