from collections import Counter
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        #sort array
        nums.sort()
        n,res,l,cur=len(nums),0,0,0
        for r in range(n):
            cur+=nums[r]
            while (r-l+1)*nums[r]-cur>k:
                cur-=nums[l]
                l+=1
            res=max(res,r-l+1)
        return res
        
