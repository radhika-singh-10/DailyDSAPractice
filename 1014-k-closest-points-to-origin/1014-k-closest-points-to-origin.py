import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res,n,min_heap=[],len(points),[]
        for i in range(n):
            a,b=points[i][0],points[i][1]
            dist=a*a+b*b
            min_heap.append((dist,a,b))
        heapq.heapify(min_heap)
        for _ in range(k):
            _,a,b=heapq.heappop(min_heap)
            res.append((a,b))
        return res