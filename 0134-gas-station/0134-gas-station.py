class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):
            return -1
        else:
            n,total,cur,res=len(gas),0,0,0
            for i in range(n):
                cur+=gas[i]-cost[i]
                if cur<0:
                    cur=0
                    res = i+1

            return res