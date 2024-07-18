class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort(reverse=True)
        processorTime.sort()
        n=len(processorTime)
        j,res=0,0
        m=int(len(tasks)/n)
        for i in range(len(tasks)):
            if i % 4 == 4:
                res = 0   
            res = max(res, processorTime[int(i/4)] + tasks[i])
                
        return res
