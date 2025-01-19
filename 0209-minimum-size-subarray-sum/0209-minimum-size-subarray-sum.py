class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n,res,l,total=len(nums),float("inf"),0,0
        for r in range(n):
            total+=nums[r]
            while total>=target:
                res=min(res,r-l+1)
                total-=nums[l]
                l=l+1

        return 0 if res==float("inf") else res

