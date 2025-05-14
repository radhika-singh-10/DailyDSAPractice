from collections import deque
#cache concept - mpontonic stack
#intuition- element smaller than larger lement that come before larger element will never be selected, so pop them out - use deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # if len(nums)<=k:
        #     return nums
        res=[]
        queue=deque()
        #queue.append(nums[0])
        for i,j in enumerate(nums):
            
            while queue and nums[queue[-1]]<j:
                queue.pop()

            queue.append(i)
            
            if queue[0] == i-k:
                queue.popleft()
            
            if i>=k-1:
                res.append(nums[queue[0]])

        return res
        
