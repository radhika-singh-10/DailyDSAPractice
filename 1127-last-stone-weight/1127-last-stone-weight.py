import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] *= -1
        heapq.heapify(stones)
        while len(stones)>1:
            stone_one=heapq.heappop(stones)
            stone_two=heapq.heappop(stones)
            if stone_one!=stone_two:
                heapq.heappush(stones,stone_one-stone_two)
        
        
        return -heapq.heappop(stones) if stones else 0
        
        