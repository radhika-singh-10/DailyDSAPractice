class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        #maxprofit, min captial ->k times-> check  cur_captial=w, cur_Captial<=start of captial
        #sort by (max profit, min captial)
        #till k>0-> cur_Capital+=profit[i] if cur_capital<=capital
        n=len(profits)
        # min capital - greedy, max profit
        capitalInfo=list(zip(capital, profits))
        capitalInfo.sort()
        queue,ptr=[],0
        while k>0:
            while ptr<n and capitalInfo[ptr][0]<=w:
                heappush(queue,-capitalInfo[ptr][1])
                ptr+=1
            if not queue:
                break
            w+=-heappop(queue)
            k-=1
        return w
        


        #capitalInfo.sort(key=lambda x:(x[0],-x[1]))
        # res,i=0,0
        # print(capitalInfo)
        # while k>0 and i<n:
        #     res+=capitalInfo[i][1]
        #     i+=1
        #     k-=1
        #     print(i,n,res,capitalInfo)
        # return res




