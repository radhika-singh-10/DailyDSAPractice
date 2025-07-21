class Solution:
    def maximumProfit(self, present: List[int], future: List[int], budget: int) -> int:
        # n = len(present)
        #top down approach - tle
        # def dfs(i, rem):
        #     if rem < 0:
        #         return float('-inf')
        #     if i >= n:
        #         return 0
        #     if (i, rem) in memo:
        #         return memo[(i, rem)]
        #     skip = dfs(i + 1, rem)
        #     profit = future[i] - present[i]
        #     new_rem = rem - present[i]
        #     pick = profit + dfs(i + 1, new_rem)
        #     memo[(i, rem)] = max(skip, pick)
        #     return memo[(i, rem)]
        # memo = dict()
        # return dfs(0, budget)
        n=len(present)
        dp = [0 for _ in range(budget + 1)]
        for f,p in zip(future,present):
            #print(p-1)
            for i in range(budget,p-1,-1):
                
                dp[i]=max(dp[i],f-p+dp[i-p])
            #print(dp)
        return dp[budget]
