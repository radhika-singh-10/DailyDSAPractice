class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n=len(costs)
        for i in range(1,n):
            costs[i][0]+=min(costs[i-1][1],costs[i-1][2])
            costs[i][1]+=min(costs[i-1][0],costs[i-1][2])
            costs[i][2]+=min(costs[i-1][0],costs[i-1][1])
        return min(costs[n-1][0],costs[n-1][1],costs[n-1][2])
        # color=[0]*n
        # #color[i]!=color[i-1] and min(color[i])
        # res=min(costs[0])
        # color[0]=costs[0].index(res)
        # for i in range(1,n):
        #     temp=costs[i][0]
        #     index=0
        #     for j in range(3):
        #         if j!=color[i-1]:
        #             temp=min(temp,costs[i][j])
        #             index=j
        #     color[i]=index
        #     res+=temp
        # return res





