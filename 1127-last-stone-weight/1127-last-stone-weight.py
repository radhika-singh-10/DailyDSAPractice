import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        n=len(stones)
        if n==1:
            return stones[0]
        else:
            #make a max heap of stones
            #till 1 stone is left in the heap
            #  remove max stone from heap
            #  if max_Stone1!=max_stone2: push in the heap
            #return last stone if heap is not empty else return 0
            for i in range(n):
                stones[i] *= -1
            heapq.heapify(stones)
            while len(stones)>1:
                stone_one,stone_two=heapq.heappop(stones),heapq.heappop(stones)
                if stone_one!=stone_two:
                    heapq.heappush(stones, stone_one - stone_two)
            return -heapq.heappop(stones) if stones else 0