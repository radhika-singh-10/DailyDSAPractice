class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #nums.sort()
        count=0
        j=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[count]=nums[i]
                count+=1
        return count
                