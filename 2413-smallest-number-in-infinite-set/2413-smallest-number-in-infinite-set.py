import heapq
class SmallestInfiniteSet:

    def __init__(self):
        self.heap=[]
        for i in range(1,1001):
            self.heap.append(i)

    def popSmallest(self) -> int:
        # for elem in self.heap:
        #     elem*=-1
        heapq.heapify(self.heap)
        # print(self.heap)
        elem=self.heap[0]
        heapq.heappop(self.heap)
        return elem


    def addBack(self, num: int) -> None:
        if num not in self.heap:
            self.heap.append(num)
        heapq.heapify(self.heap)
        



# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)