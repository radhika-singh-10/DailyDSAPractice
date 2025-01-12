import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k=k
        self.heap=[]
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        if len(self.heap)<self.k or self.heap[0]<val:
            heapq.heappush(self.heap,val)
            if len(self.heap)>self.k:
                heapq.heappop(self.heap)
        return self.heap[0]
        # self.nums.append(val)
        # heapq.heapify(self.nums)
        # val=heapq.nlargest(self.k,self.nums)
        # return val[-1]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)