class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        step_one,step_two=cost[0],cost[1]
        #min(step_one,step_two)
        min_cost=[0]*(len(cost)+1)
        
        for i in range(2,len(cost)+1):
            step_one_cost = min_cost[i-2]+cost[i-2]
            step_two_cost = min_cost[i-1]+cost[i-1]
            min_cost[i]=min(step_one_cost,step_two_cost)
        return min_cost[-1]