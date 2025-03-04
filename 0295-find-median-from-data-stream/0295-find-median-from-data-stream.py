import heapq
class MedianFinder:

    def __init__(self):
        #self.numList=[]
        self.minHeap=[]
        self.maxHeap=[]

    def addNum(self, num: int) -> None:
        #append the number in the list
        #self.numList.append(num)

        #approach-o(logn)
        #All the numbers in the max-heap are smaller or equal to the top element of the max-heap (let's call it x)
        #All the numbers in the min-heap are larger or equal to the top element of the min-heap (let's call it y)

        if len(self.minHeap)==len(self.maxHeap):
            heapq.heappush(self.maxHeap,-heapq.heappushpop(self.minHeap,-num))
            #print(num,self.minHeap,self.maxHeap)
        else:
            heapq.heappush(self.minHeap,-heapq.heappushpop(self.maxHeap,num))
            #print(num,self.minHeap,self.maxHeap)
        

    def findMedian(self) -> float:
        if len(self.minHeap)==len(self.maxHeap):
            return float(self.maxHeap[0]-self.minHeap[0])/2.0
        else:
            return float(self.maxHeap[0])
        # self.numList.sort()
        # n=len(self.numList)
        # print(self.numList)
        # mid=n//2
        # if n%2==0:
        #     return (self.numList[int(mid)-1]+self.numList[int(mid)])/2
        #     # return (self.numList[(n-1)//2]+self.numList(n+1)//2)/2
        # else:
        #     return float(self.numList[mid])

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()