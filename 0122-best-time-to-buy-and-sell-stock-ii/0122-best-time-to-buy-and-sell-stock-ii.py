class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i=1
        profit=0
        while i<len(prices):
            if prices[i]>prices[i-1] : 
                profit+=prices[i]-prices[i-1]
                print(profit,prices[i]-prices[i-1])
            i=i+1
        return profit

