class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l,res,n=0,nums[0],len(nums)
        s=nums[0]
        for r in range(1,n):
            if s<0:
                s=nums[r]
            else:
                s+=nums[r]
            res=max(s,res)
        return res
