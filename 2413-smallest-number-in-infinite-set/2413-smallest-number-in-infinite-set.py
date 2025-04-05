# import heapq
class SmallestInfiniteSet:

    def __init__(self):
        self.heap=[]
        self.isPresent=set()
        self.current=1
        #since we haev the constraint here that is why we have added 1-1000
        # for i in range(1,1001):
        #     self.heap.append(i)

    def popSmallest(self) -> int:
        # for elem in self.heap:
        #     elem*=-1
        if len(self.heap)>0:
            res=heapq.heappop(self.heap)
            self.isPresent.remove(res)
        else:
            res=self.current
            self.current+=1
        return res
        # heapq.heapify(self.heap)
        # # print(self.heap)
        # elem=self.heap[0]
        # heapq.heappop(self.heap)
        # return elem


    def addBack(self, num: int) -> None:
        if self.current<=num or num in self.isPresent:
            return
        heapq.heappush(self.heap,num)
        self.isPresent.add(num)
        # if num not in self.heap:
        #     self.heap.append(num)
        # heapq.heapify(self.heap)
        



# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)