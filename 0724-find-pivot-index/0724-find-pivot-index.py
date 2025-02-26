class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        lsum=0
        rsum=sum(nums[1:])
        for i in range(len(nums)-1): 
            if lsum==rsum:
                return i
            lsum+=nums[i]
            rsum-=nums[i+1]
        if lsum==rsum:
            return len(nums)-1
        else:
            return -1
