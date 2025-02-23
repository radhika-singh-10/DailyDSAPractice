class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i=1
        profit=0
        while i<len(prices):
            if prices[i]>prices[i-1] : 
                profit+=prices[i]-prices[i-1]
                #print(profit,prices[i]-prices[i-1])
            i=i+1
        # n,valley,peak=len(prices),prices[0],prices[0]
        # while i<n-1:
        #     while i<n-1 and prices[i]<=prices[i+1]:
        #         i+=1
        #     peak=prices[i]
        #     while i<n-1 and prices[i]>=prices[i+1]:
        #         i+=1
        #     valley=prices[i]
        #     profit+=peak-valley
        return profit
        # i = 0
        # valley = prices[0]
        # peak = prices[0]
        # maxprofit = 0
        # while i < len(prices) - 1:
        #     while i < len(prices) - 1 and prices[i] >= prices[i + 1]:
        #         i += 1
        #     valley = prices[i]
        #     while i < len(prices) - 1 and prices[i] <= prices[i + 1]:
        #         i += 1
        #     peak = prices[i]
        #     maxprofit += peak - valley
        # return maxprofit

