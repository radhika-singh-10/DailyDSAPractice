class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        n=len(cost)
        
        for i in range(1,n):
            cost[i]=min(cost[i],cost[i-1])
        return cost