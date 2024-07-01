class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=0
        i=0
        if len(nums)<=2:
            return len(nums)
        for i in nums:
            if k<2 or i!=nums[k-2]:
                nums[k]=i
                k+=1
            i=i+1
        return k