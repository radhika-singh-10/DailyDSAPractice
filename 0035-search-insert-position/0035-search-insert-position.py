class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #binary search
        l,r=0,len(nums)-1
        while l<=r:
            m=l+(r-l)//2
            if nums[m]<target:
                l=m+1
            elif nums[m]>target:
                r=m-1
            else:
                return m
        #if not found, we return the lower index
        return l
                
