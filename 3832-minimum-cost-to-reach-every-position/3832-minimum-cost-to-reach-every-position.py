class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        n=len(cost)
        answer=cost
        for i in range(1,n):
            answer[i]=min(answer[i],cost[i-1])
        return answer