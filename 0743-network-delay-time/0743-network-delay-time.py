
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        dist = [float('inf')] * (n + 1)
        dist[k]=0
        for _ in range(n - 1):
            for src,dst,time in times:
                if dist[src]+time<dist[dst]:
                    dist[dst]=dist[src]+time
        dist[0]=0
        res=max(dist)
        print(res,dist)
        return res if res<float('inf') else -1



        