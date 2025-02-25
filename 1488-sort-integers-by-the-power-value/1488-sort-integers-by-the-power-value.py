import heapq
class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        memo = {1:0}
        def transform(x):
            if x in memo:
                return memo[x]
            val = None
            if x%2 == 0:
                val = transform(x//2) + 1
            else:
                val = transform(3*x + 1) + 1
            memo[x] = val
            return memo[x]
        
        heap = []
        for x in range(lo, hi+1):
            heapq.heappush(heap, (-transform(x), -x))
            if len(heap) > k:
                heapq.heappop(heap)
        return -heap[0][1]