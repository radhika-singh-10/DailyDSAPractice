class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n=len(arr)
        if n==1:
            return arr
        res=[]
        heap=[]
        for i in range(n):
            diff=abs(arr[i]-x)
            heapq.heappush(heap,[diff,arr[i]])
        for i in range(k):
            diff,val=heapq.heappop(heap)
            res.append(val)
        
        return sorted(res)
        # l,r=0,len(arr)-1
        # while r-l>=k:
        #     if (abs(arr[l]-x)<=abs(arr[r]-x)) :
        #         r-=1
        #     else:
        #         l+=1

        # for i in range(l,r+1):
        #     res.append(arr[i])
        # return res
        # res,n,min_heap=[],len(arr),[]
        # for i in range(n-1):
        #     a,b=arr[i],arr[i+1]
        #     dist=a*a+b*b
        #     min_heap.append((dist,a,b))
        # heapq.heapify(min_heap)
        # for _ in range(k):
        #     _,a,b=heapq.heappop(min_heap)
        #     res.append((a,b))
        # return res