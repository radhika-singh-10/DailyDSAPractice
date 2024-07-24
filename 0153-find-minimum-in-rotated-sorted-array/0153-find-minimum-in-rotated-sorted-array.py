class Solution:
    def findMin(self, nums: List[int]) -> int:
        rotate_count=0
        l,r=0,len(nums)-1
        res=nums[0]
        while l<r:
            m=l+(r-l)//2
            res=min(res,nums[m])
            if nums[m]<nums[r]:
                r=m
            else:
                l=m+1

        return nums[l]

