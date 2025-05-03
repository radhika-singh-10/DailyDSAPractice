class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #mock question. - meta
        n=len(nums)
        l,r=0,n-1
        while l<=r:
            m=l+(r-l)//2
            if nums[m]==target:
                return m
            elif nums[m]>=nums[l]:
                if nums[l]<=target and nums[m]>target:
                    r=m-1
                else:
                    l=m+1
            else:
                if nums[r]>=target and nums[m]<target:
                    l=m+1
                else:
                    r=m-1

        return -1