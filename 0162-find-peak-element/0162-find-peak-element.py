class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        #binary search
        l,r,peak=0,len(nums)-1,0
        if len(nums)==1:
            return 0
        elif len(nums)==2 and nums[0]<nums[1]:
            return 1
        elif len(nums)==2 and nums[0]>nums[1]:
            return 0
        while l<r:
            m=l+(r-l)//2
            if nums[m]>nums[m+1]:
                r=m
            else:
                l=m+1

        return l

        