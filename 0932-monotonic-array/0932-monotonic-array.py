class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n,increasing,decreasing=len(nums),True,True
        for i in range(n-1):
            if nums[i]>nums[i+1]:
                increasing=False
            if nums[i]<nums[i+1]:
                decreasing=False
        return increasing or decreasing
                
