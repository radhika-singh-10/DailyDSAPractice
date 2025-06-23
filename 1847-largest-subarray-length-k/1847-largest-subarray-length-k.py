class Solution:
    def largestSubarray(self, nums: List[int], k: int) -> List[int]:
        n,tempArr=len(nums),[]
        maxIndex=0
        for i in range(1,n-(k-1)):
            if nums[i]>nums[maxIndex]:
                maxIndex=i
        return nums[maxIndex:maxIndex+k]


