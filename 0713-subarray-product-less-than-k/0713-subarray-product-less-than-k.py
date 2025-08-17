class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1 or k<min(nums):
            return 0
        n=len(nums)
        res=0
        l,mul=0,1
        for r in range(n):
            mul*=nums[r]
            while mul>=k:
                mul//=nums[l]
                l+=1
            res+=r-l+1
        return res
            
            