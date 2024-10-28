import sys
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        n=len(nums)
        if k==1:
            return 0
        nums.sort()
        min_diff=max(nums)
        for i in range(n-k+1):
            min_diff=min(min_diff,abs(nums[i]-nums[i+k-1]))
        return min_diff

        
        
            