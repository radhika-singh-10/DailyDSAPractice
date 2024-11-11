class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        #binary search
        l,r,peak=0,len(nums)-1,0
        while l<r:
            m=l+(r-l)//2
            if nums[m]>nums[m-1] and nums[m]>nums[m+1]:
                return m
            elif nums[m]<nums[m-1]:
                r=m-1
            else:
                l=m+1

        return peak

        