class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit,n=0,len(prices)
        left_min,right_max=prices[0],prices[-1]
        left_profits,right_profits=[0]*n,[0]*(n+1)
        for l in range(1, n):
            left_profits[l] = max(left_profits[l - 1], prices[l] - left_min)
            left_min = min(left_min, prices[l])
            r = n - 1 - l
            right_profits[r] = max(right_profits[r + 1], right_max - prices[r])
            right_max = max(right_max, prices[r])
        res=0
        for i in range(n):
            res=max(res,left_profits[i]+right_profits[i+1])
        return res



