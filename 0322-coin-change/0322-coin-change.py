from functools import lru_cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # n=len(coins)
        # if amount==0 or n==0:
        #     return 0
        # if min(coins)>amount:
        #     return -1
        #dp=[[0]*(n+1) for i in range(amount)]
        @lru_cache(None)
        def dfs(rem):
            if rem < 0:
                return -1
            if rem == 0:
                return 0
            min_cost = float('inf')
            for coin in coins:
                res = dfs(rem - coin)
                if res != -1:
                    min_cost = min(min_cost, res + 1)
            return min_cost if min_cost != float('inf') else -1

        return dfs(amount)