class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        res,j=0,1
        for i in range(1,len(nums)):
            if nums[i-1]!=nums[i]:
                nums[j]=nums[i]
                j+=1
                res+=1

        return res+1

        