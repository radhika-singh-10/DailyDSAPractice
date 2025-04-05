class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        job_info=[(difficulty[i],profit[i]) for i in range(len(difficulty))]
        worker.sort()
        job_info.sort()
        res,max_profit,i=0,0,0
        for w in worker:
            while i<len(difficulty) and w>=job_info[i][0]:
                max_profit=max(max_profit,job_info[i][1])
                i+=1
            res+=max_profit
        return res