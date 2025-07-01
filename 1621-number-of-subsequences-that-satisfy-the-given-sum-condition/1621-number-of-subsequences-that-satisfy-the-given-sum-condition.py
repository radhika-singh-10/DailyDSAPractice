class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        l,r,n=0,len(nums)-1,len(nums)
        res,mod =0, 10 ** 9 + 7
        while l<=r:
            if nums[l]+nums[r]<=target:
                res=(res+pow(2,r-l,mod))%mod
                l+=1
            else:
                r-=1
        return res