class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        n,res=len(nums),float('inf')
        for l in range(n):
            or_res=0
            for r in range(l,n):
                or_res|=nums[r]
                if or_res>=k:
                    res=min(res,r-l+1)
                    break
        return res if res!=float('inf') else -1
                

