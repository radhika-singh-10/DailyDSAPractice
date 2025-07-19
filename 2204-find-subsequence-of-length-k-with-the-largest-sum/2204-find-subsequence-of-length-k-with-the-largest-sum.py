class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        heap=[]
        for i,num in enumerate(nums):
            heapq.heappush(heap,(num,i))
            if len(heap)>k:
                heapq.heappop(heap)
        idx = sorted([i for _,i in heap])
        return [nums[i] for i in idx]
